from typing import Dict, Any
from tqdm import tqdm
import geopandas as gpd

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.metadata import post_to_object
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
    crs = ""
    for prediction_object_name in tqdm(list_of_prediction_objects):
        logger.info(f"processing {prediction_object_name} ...")

        object_metadata[prediction_object_name] = {"success": False}

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
            if row["building_id"] in unique_ids:
                # ToDO: create building_id-metadata
                ...
            else:
                # ToDO: update building_id-metadata

                unique_polygons.append(row["geometry"])
                unique_ids.append(row["building_id"])

        object_metadata[prediction_object_name] = {
            "success": True,
            "building_count": len(gdf),
        }
        success_count += 1

    output_gdf = gpd.GeoDataFrame(
        data={
            "building_id": unique_ids,
            "geometry": unique_polygons,
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
        },
    )
