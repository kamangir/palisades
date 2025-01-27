from typing import List

from blue_options.terminal import show_usage, xtra


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("acq_count=<-1>,building_count=<-1>,dryrun,", mono=mono),
            "upload",
        ]
    )

    return show_usage(
        [
            "palisades",
            "analytics",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "ingest analytics.",
        mono=mono,
    )


def help_ingest_building(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "building=<building-id>",
            xtra(",~download,dryrun,", mono=mono),
            "upload",
        ]
    )

    return show_usage(
        [
            "palisades",
            "analytics",
            "ingest_building",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "ingest building analytics.",
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
    "ingest_building": help_ingest_building,
}
