from typing import Dict, Any
from tqdm import tqdm, trange
import geopandas as gpd
import numpy as np

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.metadata import post_to_object, get_from_object
from blue_objects.mlflow.tags import create_filter_string

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
    list_of_buildings: Dict[str, Any] = {}
    success_count: int = 0
    list_of_polygons = []
    list_of_building_ids = []
    list_of_thumbnail = []
    list_of_thumbnail_object = []
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

        if not objects.download(
            filename="analysis.gpkg",
            object_name=prediction_object_name,
        ):
            continue

        success, gdf = file.load_geodataframe(
            objects.path_of(
                filename="analysis.gpkg",
                object_name=prediction_object_name,
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
            if row["building_id"] not in list_of_building_ids:
                list_of_buildings[row["building_id"]] = {}

                list_of_building_ids.append(row["building_id"])
                list_of_polygons.append(row["geometry"])
                list_of_thumbnail.append(row["thumbnail"])
                list_of_thumbnail_object.append(prediction_object_name)

            list_of_buildings[row["building_id"]][prediction_datetime] = {
                "area": row["area"],
                "damage": row["damage"],
                "thumbnail": row["thumbnail"],
                "object_name": prediction_object_name,
            }

        object_metadata[prediction_object_name] = {
            "success": True,
            "building_count": len(gdf),
        }
        success_count += 1

    observation_count: Dict[int:int] = {}
    for building_metadata in list_of_buildings.values():
        observation_count[len(building_metadata)] = (
            observation_count.get(len(building_metadata), 0) + 1
        )
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
            "area": [
                float(
                    np.mean(
                        [
                            building_info["area"]
                            for building_info in building_metadata.values()
                        ]
                    )
                )
                for building_metadata in list_of_buildings.values()
            ],
            "area_std": [
                float(
                    np.std(
                        [
                            building_info["area"]
                            for building_info in building_metadata.values()
                        ]
                    )
                )
                for building_metadata in list_of_buildings.values()
            ],
            "damage": [
                float(
                    np.mean(
                        [
                            building_info["damage"]
                            for building_info in building_metadata.values()
                        ]
                    )
                )
                for building_metadata in list_of_buildings.values()
            ],
            "damage_std": [
                float(
                    np.std(
                        [
                            building_info["damage"]
                            for building_info in building_metadata.values()
                        ]
                    )
                )
                for building_metadata in list_of_buildings.values()
            ],
            "thumbnail": list_of_thumbnail,
            "thumbnail_object": list_of_thumbnail_object,
            "observation_count": [
                len(building_metadata)
                for building_metadata in list_of_buildings.values()
            ],
        },
    )
    output_gdf.crs = crs
    geojson_filename = objects.path_of(
        "analytics.geojson",
        object_name,
    )
    output_gdf.to_file(
        geojson_filename,
        driver="GeoJSON",
    )

    logger.info(
        "{} object(s) -> {} ingested -> {:,} buildings(s) -> {}.".format(
            len(object_metadata),
            success_count,
            len(output_gdf),
            file.name_and_extension(geojson_filename),
        )
    )

    return post_to_object(
        object_name,
        "analytics",
        {
            "list_of_buildings": list_of_buildings,
            "building_count": len(list_of_buildings),
            "objects": object_metadata,
            "observation_count": observation_count,
        },
    )
