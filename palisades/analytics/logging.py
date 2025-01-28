from typing import Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from blue_objects import file, objects

from blue_objects.graphics.signature import sign_filename

from palisades.host import signature
from palisades.logger import logger


def log_analytics(
    df: pd.DataFrame,
    metadata: Dict,
    object_name: str,
) -> bool:
    plt.figure(figsize=(10, 5))
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
    row: pd.DataFrame,
    list_of_prediction_datetime: List[str],
    object_name: str,
) -> bool:
    building_id = str(row["building_id"].values[0])

    plt.figure(figsize=(10, 5))

    list_of_damage_values = row[list_of_prediction_datetime]

    history = [
        (prediction_date_time, float(damage_value))
        for prediction_date_time, damage_value in zip(
            list_of_prediction_datetime, list_of_damage_values.squeeze()
        )
        if not np.isnan(damage_value)
    ]

    logger.info(f"{len(history)} acquisition(s)")
    for index, item in enumerate(history):
        logger.info(
            "#{:02d}: {} - {:.1f}%".format(
                index + 1,
                item[0],
                100 * item[1],
            )
        )

    plt.bar(
        range(len(history)),
        [item[1] for item in history],
        color="gray",
    )
    plt.title(f"Damage History | {building_id}")
    plt.xlabel("Acquisition Date")
    plt.ylabel("Damage")
    plt.ylim(0, 1)
    plt.xticks(
        range(len(history)),
        [item[0] for item in history],
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
