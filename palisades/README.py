import os

from blue_options.help.functions import get_help
from blue_objects import file, README
from blue_geo import ICON as blue_geo_ICON
from roofai import ICON as roofai_ICON

from palisades.help.functions import help_functions
from palisades import NAME, VERSION, ICON, REPO_NAME, MARQUEE

# refactor

list_of_menu_item = {
    "STAC Catalog: Maxar Open Data": {
        "ICON": blue_geo_ICON,
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data",
        "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true",
        "title": '["Satellite imagery for select sudden onset major crisis events"](https://www.maxar.com/open-data/)',
    },
    "Vision Algo: Semantic Segmentation": {
        "ICON": roofai_ICON,
        "url": "https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md",
        "marquee": "https://github.com/kamangir/assets/raw/main/palisades/prediction-lres.png?raw=true",
        "title": "[segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch)",
    },
    "Building Damage Analysis": {
        "ICON": ICON,
        "url": "https://github.com/kamangir/palisades/blob/main/palisades/docs/building-analysis.md",
        "marquee": "https://github.com/kamangir/assets/blob/main/palisades/building-analysis-5.png?raw=true",
        "title": "using Microsoft, OSM, and Google footprints through [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment)",
    },
    "Analytics": {
        "ICON": ICON,
        "url": "https://github.com/kamangir/palisades/blob/main/palisades/docs/damage-analytics.md",
        "marquee": "https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2.png?raw=true",
        "title": "Damage information for multi-datacube areas.",
    },
    "template": {
        "ICON": ICON,
        "url": "#",
        "marquee": "",
        "title": "",
    },
}


items = [
    "{}[`{}`]({}) [![image]({})]({}) {}".format(
        menu_item["ICON"],
        menu_item_name,
        menu_item["url"],
        menu_item["marquee"],
        menu_item["url"],
        menu_item["title"],
    )
    for menu_item_name, menu_item in list_of_menu_item.items()
    if menu_item_name != "template"
]


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for readme in [
            {
                "cols": 2,
                "items": items,
                "path": "..",
            },
            {
                "path": "docs/step-by-step.md",
            },
            {
                "path": "docs/release-one.md",
            },
            {
                "path": "docs/building-analysis.md",
            },
            {
                "path": "docs/damage-analytics.md",
            },
        ]
    )
