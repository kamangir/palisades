from typing import Dict, List, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from palisades import NAME
from blueness import module
from blue_objects import file, objects
from blue_objects.graphics.signature import sign_filename

from palisades.host import signature
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def log_analytics(
    df: pd.DataFrame,
    metadata: Dict,
    object_name: str,
) -> bool:
    if df.empty:
        logger.warning(f"{NAME}.log_analytics: empty dataframe, skipped.")
        return True

    plt.figure(figsize=(15, 5))
    df[metadata["datetime"]].count().plot(
        kind="bar",
        color="gray",
    )
    plt.title("Damage History")
    plt.xlabel("Acquisition Date")
    plt.ylabel("Damaged Building Count")
    plt.xticks(
        range(len(metadata["datetime"])),
        metadata["datetime"],
        rotation=90,
    )
    plt.grid(True)
    filename = objects.path_of(
        "damage-history.png",
        object_name,
    )
    return file.save_fig(filename) and sign_filename(
        filename=filename,
        header=[
            "{} acquisition(s)".format(
                len(metadata["datetime"]),
            ),
        ]
        + objects.signature(object_name=object_name),
        footer=signature(),
    )


def log_building_analytics(
    building_id: str,
    history: Dict[str, float],
    list_of_prediction_datetime: List[str],
    object_name: str,
) -> bool:
    plt.figure(figsize=(15, 5))

    logger.info(f"{len(history)} acquisition(s)")
    for index, (prediction_date_time, damage_value) in enumerate(history.items()):
        logger.info(
            "#{:02d}: {} - {:.1f}%".format(
                index + 1,
                prediction_date_time,
                100 * damage_value,
            )
        )

    plt.bar(
        range(len(history)),
        list(history.values()),
        color="gray",
    )
    plt.title(f"Damage History | {building_id}")
    plt.xlabel("Acquisition Date")
    plt.ylabel("Damage")
    plt.ylim(0, 1)
    plt.xticks(
        range(len(history)),
        list(history.keys()),
        rotation=90,
    )
    plt.grid(True)
    filename = objects.path_of(
        "thumbnail-{}-damage-history.png".format(building_id),
        object_name,
    )
    return file.save_fig(filename) and sign_filename(
        filename=filename,
        header=[
            building_id,
            f"{len(history)} acquisition(s)",
        ]
        + objects.signature(object_name=object_name),
        footer=signature(),
    )
