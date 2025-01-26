from typing import Dict, Any
from tqdm import tqdm, trange
import geopandas as gpd
import glob
import shutil

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.metadata import post_to_object, get_from_object
from blue_objects.mlflow.tags import create_filter_string
from blue_objects.graphics.gif import generate_animated_gif

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def ingest_analytics(
    object_name: str,
    generate_gifs: bool = False,
    acq_count: int = -1,
    building_count: int = -1,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest_analytics -{}{}> {}".format(
            NAME,
            f"{acq_count} acq(s)-" if acq_count != -1 else "",
            f"{building_count} buildings(s)-" if building_count != -1 else "",
            object_name,
        )
    )

    list_of_prediction_objects = mlflow.search(
        create_filter_string("contains=palisades.prediction,profile=FULL")
    )
    if acq_count != -1:
        list_of_prediction_objects = list_of_prediction_objects[:acq_count]
    logger.info(f"{len(list_of_prediction_objects)} acq(s) to process.")

    object_metadata: Dict[str, Any] = {}
    success_count: int = 0
    list_of_polygons = []
    list_of_building_ids = []
    list_of_area = []
    list_of_damage = []
    list_of_thumbnail = []
    crs = ""
    for prediction_object_name in tqdm(list_of_prediction_objects):
        logger.info(f"processing {prediction_object_name} ...")

        object_metadata[prediction_object_name] = {"success": False}

        prediction_datetime = get_from_object(
            prediction_object_name,
            "analysis.datetime",
            download=True,
        )
        if not prediction_datetime:
            logger.warning("analysis.datetime not found.")
            continue

        if generate_gifs:
            if not objects.download(prediction_object_name):
                continue

            for filename in tqdm(
                glob.glob(
                    objects.path_of(
                        "thumbnail-*.png",
                        prediction_object_name,
                    )
                )
            ):
                shutil.copy(
                    filename,
                    objects.path_of(
                        file.name_and_extension(filename),
                        object_name,
                    ),
                )

        success, gdf = file.load_geodataframe(
            objects.path_of(
                "analysis.gpkg",
                prediction_object_name,
            ),
            log=verbose,
        )
        if not success:
            continue
        if not crs:
            crs = gdf.crs
        if building_count != -1:
            gdf = gdf.head(building_count)

        if "building_id" not in gdf.columns:
            logger.warning("building_id not found.")
            continue

        for _, row in tqdm(gdf.iterrows()):
            building_metadata: Dict[str, Any] = {}
            building_metadata_filename = objects.path_of(
                "metadata-{}.yaml".format(row["building_id"]),
                object_name,
            )

            if row["building_id"] in list_of_building_ids:
                success, building_metadata = file.load_yaml(building_metadata_filename)
                assert success
            else:
                list_of_thumbnail.append(row["thumbnail"])
                list_of_polygons.append(row["geometry"])
                list_of_building_ids.append(row["building_id"])
                list_of_area.append(row["area"])
                list_of_damage.append(row["damage"])

            building_metadata[prediction_datetime] = {
                "area": row["area"],
                "damage": row["damage"],
                "thumbnail": row["thumbnail"],
                "object_name": prediction_object_name,
            }
            assert file.save_yaml(
                building_metadata_filename,
                building_metadata,
                log=verbose,
            )

        object_metadata[prediction_object_name] = {
            "success": True,
            "building_count": len(gdf),
        }
        success_count += 1

    if generate_gifs:
        logger.info("generating combined views...")
    observation_count: Dict[int:int] = {}
    for index in trange(len(list_of_building_ids)):
        building_id = list_of_building_ids[index]

        success, building_metadata = file.load_yaml(
            objects.path_of(
                f"metadata-{building_id}.yaml",
                object_name,
            )
        )
        assert success

        observation_count[len(building_metadata)] = (
            observation_count.get(len(building_metadata), 0) + 1
        )

        if len(building_metadata) > 1 and generate_gifs:
            thumbnail_filename = objects.path_of(
                f"thumbnail-{building_id}-{object_name}.gif",
                object_name,
            )

            list_of_images = [
                objects.path_of(
                    building_metadata[datacube_datetime]["thumbnail"],
                    building_metadata[datacube_datetime]["object_name"],
                )
                for datacube_datetime in building_metadata
            ]

            assert generate_animated_gif(
                list_of_images=list_of_images,
                output_filename=thumbnail_filename,
                frame_duration=1000,
                log=verbose,
            )

            for filename in list_of_images:
                assert file.delete(filename)

            list_of_thumbnail[index] = file.name_and_extension(thumbnail_filename)
    logger.info(
        "observation counts: {}".format(
            ", ".join(
                [f"{rounds}X: {count}" for rounds, count in observation_count.items()]
            )
        )
    )

    output_gdf = gpd.GeoDataFrame(
        data={
            "building_id": list_of_building_ids,
            "geometry": list_of_polygons,
            "area": list_of_area,
            "damage": list_of_damage,
            "thumbnail": list_of_thumbnail,
        },
    )
    output_gdf.crs = crs
    output_gdf.to_file(
        objects.path_of(
            "analytics.geojson",
            object_name,
        ),
        driver="GeoJSON",
    )

    logger.info(
        "{} object(s) -> {} ingested -> {:,} buildings(s).".format(
            len(object_metadata),
            success_count,
            len(output_gdf),
        )
    )

    return post_to_object(
        object_name,
        "analytics.ingest",
        {
            "objects": object_metadata,
            "observation_count": observation_count,
        },
    )
