from typing import Dict
from tqdm import tqdm
import pandas as pd

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import get_from_object, post_to_object
from blue_objects.graphics.gif import generate_animated_gif

from palisades import NAME
from palisades.analytics.logging import log_building_analytics
from palisades.analytics.collection import collect_analytics
from palisades.logger import logger
from typing import List

NAME = module.name(__file__, NAME)


def ingest_building(
    object_name: str,
    building_id: str,
    acq_count: int = -1,
    building_count: int = -1,
    do_deep: bool = False,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest_building: {} @ {}{}".format(
            NAME,
            building_id,
            object_name,
            " - 🤿  deep" if do_deep else "",
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

    if do_deep:
        df, _, _, metadata = collect_analytics(
            acq_count=acq_count,
            building_count=building_count,
            damage_threshold=-1,
            building_id=building_id,
            log=log,
            verbose=verbose,
        )

        list_of_prediction_datetime = metadata["datetime"]
    else:
        success, df = file.load_dataframe(
            objects.path_of(
                "analytics.csv",
                object_name,
            ),
            log=log,
        )
        if not success:
            return False

        list_of_prediction_datetime = get_from_object(
            object_name,
            "analytics.datetime",
        )

    if building_id not in df["building_id"].values:
        logger.warning(f"{building_id}: building-id not found.")
        return True
    row = df[df["building_id"] == building_id]

    list_of_images: List[str] = []
    for prediction_datetime in tqdm(list_of_prediction_datetime):
        thumbnail_filename = str(row[f"{prediction_datetime}-thumbnail"].values[0])
        if thumbnail_filename == "nan":
            continue

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

    if not file.save_geojson(
        geojson_filename,
        gdf,
        log=log,
    ):
        return False

    history: Dict[str, float] = {
        prediction_date_time: float(damage_value)
        for prediction_date_time, damage_value in zip(
            list_of_prediction_datetime,
            row[list_of_prediction_datetime].values.squeeze(),
        )
        if not pd.isna(damage_value)
    }

    if not log_building_analytics(
        building_id=building_id,
        history=history,
        list_of_prediction_datetime=list_of_prediction_datetime,
        object_name=object_name,
    ):
        return False

    return post_to_object(
        object_name,
        building_id,
        {
            "history": history,
        },
    )
