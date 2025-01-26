from typing import Dict, Any
from tqdm import tqdm
import geopandas as gpd

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.metadata import post_to_object, get_from_object
from blue_objects.mlflow.tags import create_filter_string
from blue_objects.storage import instance as storage

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def ingest_analytics(
    object_name: str,
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
    unique_polygons = []
    unique_ids = []
    area_values = []
    damage_values = []
    crs = ""
    observation_count: Dict[int:int] = {}
    for prediction_object_name in tqdm(list_of_prediction_objects):
        logger.info(f"processing {prediction_object_name} ...")

        object_metadata[prediction_object_name] = {"success": False}

        prediction_datetime = get_from_object(
            prediction_object_name,
            "analysis.datetime",
        )
        if not prediction_datetime:
            logger.warning("analysis.datetime not found.")
            continue

        if not storage.exists(f"{prediction_object_name}/analysis.gpkg"):
            logger.warning("analysis.gkpg not found.")
            continue

        if not storage.download_file(
            object_name=f"bolt/{prediction_object_name}/analysis.gpkg",
            filename="object",
            log=verbose,
        ):
            continue

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

            if row["building_id"] in unique_ids:
                success, building_metadata = file.load_yaml(building_metadata_filename)
                assert success
            else:
                unique_polygons.append(row["geometry"])
                unique_ids.append(row["building_id"])
                area_values.append(row["area"])
                damage_values.append(row["damage"])

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

            observation_count[len(building_metadata)] = (
                observation_count.get(len(building_metadata), 0) + 1
            )

        object_metadata[prediction_object_name] = {
            "success": True,
            "building_count": len(gdf),
        }
        success_count += 1

    output_gdf = gpd.GeoDataFrame(
        data={
            "building_id": unique_ids,
            "geometry": unique_polygons,
            "area": area_values,
            "damage": damage_values,
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

    logger.info(
        "observation counts: {}".format(
            ", ".join(
                [f"{rounds}X: {count}" for rounds, count in observation_count.items()]
            )
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
