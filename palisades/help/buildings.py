from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions


def help_download(
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

    query_options = "".join(
        [
            "country_code=<iso-code>",
            xtra(",country_name=<country-name>,overwrite,", mono=mono),
            "source=<source>",
        ]
    )

    return show_usage(
        [
            "palisades",
            "buildings",
            "download",
            f"[{options}]",
            "[.|<input-object-name>]",
            f"[{query_options}]",
            "[-|<output-object-name>]",
        ],
        "aoi:<input-object-name>/<filename> -download-buildings-> <output-object-name>.",
        {
            "country-name: for Microsoft, optional, overrides <iso-code>.": [],
            "iso-code: Country Alpha2 ISO code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes": [
                "Canada: CA",
                "US: US",
            ],
            "source: microsoft | osm | google": [],
            "calls: https://github.com/microsoft/building-damage-assessment/blob/main/download_building_footprints.py": [],
        },
        mono=mono,
    )


help_functions = {
    "download": help_download,
}
