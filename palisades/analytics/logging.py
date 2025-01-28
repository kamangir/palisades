from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt

from blue_objects import file, objects

from blue_objects.graphics.signature import sign_filename

from palisades.host import signature


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
