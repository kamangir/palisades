from typing import List

from blue_options.terminal import show_usage, xtra


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("acq=<-1>,buildings=<-1>,dryrun,", mono=mono),
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


def help_render(
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
            "render",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "render analytics.",
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
    "render": help_render,
}
