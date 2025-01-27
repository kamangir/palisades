import geopandas as gpd
from tqdm import tqdm

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import get_from_object
from blue_objects.graphics.gif import generate_animated_gif

from palisades import NAME
from palisades.analytics.collection import collect_analytics
from palisades.logger import logger
from typing import List

NAME = module.name(__file__, NAME)


def ingest_building(
    object_name: str,
    building_id: str,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest_building: {} @ {}".format(
            NAME,
            building_id,
            object_name,
        )
    )

    geojson_filename = objects.path_of(
        "analytics.geojson",
        object_name,
    )
    success, gdf = file.load_geodataframe(
        geojson_filename,
        log=log,
    )
    if not success:
        return success

    success, df = file.load_dataframe(
        objects.path_of(
            "analytics.csv",
            object_name,
        ),
        log=log,
    )
    if not success:
        return False

    if building_id not in df["building_id"].values:
        logger.error(f"{building_id}: building-id not found.")
        return False
    row = df[df["building_id"] == building_id]

    list_of_prediction_datetime = get_from_object(
        object_name,
        "analytics.datetime",
    )

    list_of_images: List[str] = []
    for prediction_datetime in tqdm(list_of_prediction_datetime):
        thumbnail_filename = str(row[f"{prediction_datetime}-thumbnail"].values[0])
        thumbnail_object_name = str(row[f"{prediction_datetime}-object_name"].values[0])

        if not objects.download(
            filename=thumbnail_filename,
            object_name=thumbnail_object_name,
        ):
            return False

        list_of_images += [
            objects.path_of(
                filename=thumbnail_filename,
                object_name=thumbnail_object_name,
            )
        ]

    thumbnail_filename = f"thumbnail-{building_id}-{object_name}.gif"

    if not generate_animated_gif(
        list_of_images=list_of_images,
        output_filename=objects.path_of(
            thumbnail_filename,
            object_name,
        ),
        frame_duration=1000,
        log=log,
    ):
        return False

    gdf.loc[gdf["building_id"] == building_id, "thumbnail"] = thumbnail_filename
    gdf.loc[gdf["building_id"] == building_id, "thumbnail_object"] = object_name

    return file.save_geojson(
        geojson_filename,
        gdf,
        log=log,
    )
