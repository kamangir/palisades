from typing import List

from blue_options.terminal import show_usage, xtra
from roofai.help.semseg import (
    train_options,
    device_and_profile_details,
    predict_options,
)

from blue_geo.watch.targets.target_list import TargetList
from blue_geo.help.datacube import scope_details
from blue_geo.help.datacube import ingest_options as datacube_ingest_options
from blue_geo.help.datacube.label import options as datacube_label_options

target_list = TargetList(catalog="maxar_open_data")


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun", mono=mono)

    target_options = "".join(
        [
            "target=<target>",
            xtra(" | <query-object-name>", mono),
        ]
    )

    ingest_options = "".join(
        [
            xtra("~ingest_datacubes | ", mono=mono),
            datacube_ingest_options(mono=mono),
        ]
    )

    return show_usage(
        [
            "palisades",
            "ingest",
            f"[{options}]",
            f"[{target_options}]",
            f"[{ingest_options}]",
        ],
        "ingest <target>.",
        {
            "target: {}".format(" | ".join(target_list.get_list())): [],
            **scope_details,
        },
        mono=mono,
    )


def help_label(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "download,offset=<offset>"

    return show_usage(
        [
            "palisades",
            "label",
            f"[{options}]",
            f"[{datacube_label_options(mono=mono)}]",
            "[.|<query-object-name>]",
        ],
        "label <query-object-name>.",
        mono=mono,
    )


def help_predict(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "ingest",
            xtra(",~tag", mono=mono),
        ]
    )

    return show_usage(
        [
            "palisades",
            "predict",
            f"[{options}]",
            f"[{predict_options(mono=mono)}]",
            "[..|<model-object-name>]",
            "[.|<datacube-id>]",
            "[-|<prediction-object-name>]",
        ],
        "<datacube-id> -<model-object-name>-> <prediction-object-name>",
        device_and_profile_details,
        mono=mono,
    )


def help_train(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,~download,review", mono=mono)

    ingest_options = "".join(
        [
            "count=<10000>",
            xtra(",dryrun,upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "palisades",
            "train",
            f"[{options}]",
            "[.|<query-object-name>]",
            f"[{ingest_options}]",
            "[-|<dataset-object-name>]",
            "[{},epochs=<5>]".format(
                train_options(
                    mono=mono,
                    show_download=False,
                )
            ),
            "[-|<model-object-name>]",
        ],
        "train palisades.",
        device_and_profile_details,
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
    "label": help_label,
    "predict": help_predict,
    "train": help_train,
}
