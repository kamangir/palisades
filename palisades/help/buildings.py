from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions


def analyze_options(
    mono: bool,
    cascade: bool = False,
):
    return "".join(
        [xtra("buffer=<buffer>,count=<count>", mono=mono)]
        + (
            []
            if cascade
            else [
                xtra(",~download,dryrun,~ingest,", mono=mono),
                "upload",
            ]
        )
    )


analyze_details = {
    "buffer: in meters.": [],
}


def help_analyze(
    tokens: List[str],
    mono: bool,
) -> str:

    return show_usage(
        [
            "palisades",
            "buildings",
            "analyze",
            f"[{analyze_options(mono=mono)}]",
            "[.|<object-name>]",
        ],
        "analyze the buildings in <object-name>.",
        analyze_details,
        mono=mono,
    )


def query_options(mono: bool):
    return xtra(
        "country_code=<iso-code>,country_name=<country-name>,overwrite,source=<source>",
        mono=mono,
    )


query_details = {
    "country-name: for Microsoft, optional, overrides <iso-code>.": [],
    "iso-code: Country Alpha2 ISO code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes": [
        "Canada: CA",
        "US: US",
    ],
    "source: microsoft | osm | google": [],
    "calls: https://github.com/microsoft/building-damage-assessment/blob/main/download_building_footprints.py": [],
}


def help_download_footprints(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "filename=<filename>",
            xtra(",upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "palisades",
            "buildings",
            "download_footprints",
            f"[{options}]",
            "[.|<input-object-name>]",
            f"[{query_options(mono=mono)}]",
            "[-|<output-object-name>]",
        ],
        "aoi:<input-object-name>/<filename> -download-building-footprints-> <output-object-name>.",
        query_details,
        mono=mono,
    )


help_functions = {
    "analyze": help_analyze,
    "download_footprints": help_download_footprints,
}
