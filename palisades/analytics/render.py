import geopandas as gpd

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import get_from_object
from blue_objects.graphics.gif import generate_animated_gif

from palisades import NAME
from palisades.logger import logger
from typing import List

NAME = module.name(__file__, NAME)


def render_analytics(
    object_name: str,
    building_id: str,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.render_analytics: {} @ {}".format(
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

    list_of_buildings = get_from_object(
        object_name,
        "analytics.list_of_buildings",
        [],
    )
    if building_id not in list_of_buildings:
        logger.error(f"{building_id}: building-id not found.")
        return False
    building_metadata = list_of_buildings[building_id]

    list_of_images: List[str] = []
    for prediction_info in building_metadata.values():
        if not objects.download(
            filename=prediction_info["thumbnail"],
            object_name=prediction_info["object_name"],
        ):
            return False

        list_of_images += [
            objects.path_of(
                filename=prediction_info["thumbnail"],
                object_name=prediction_info["object_name"],
            )
        ]

    thumbnail_filename = objects.path_of(
        f"thumbnail-{building_id}-{object_name}.gif",
        object_name,
    )

    if not generate_animated_gif(
        list_of_images=list_of_images,
        output_filename=thumbnail_filename,
        frame_duration=1000,
        log=verbose,
    ):
        return False

    gdf.loc[gdf["building_id"] == building_id, "thumbnail"] = file.name_and_extension(
        thumbnail_filename
    )

    return True

    return file.save_geojson(
        geojson_filename,
        gdf,
        log=log,
    )
