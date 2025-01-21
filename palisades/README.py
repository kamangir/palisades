import os

from blue_objects import file, README
from blue_geo import ICON as blue_geo_ICON
from roofai import ICON as roofai_ICON

from palisades import NAME, VERSION, ICON, REPO_NAME, MARQUEE

# refactor

list_of_menu_item = {
    "STAC Catalog: Maxar Open Data": {
        "ICON": blue_geo_ICON,
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data",
        "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true",
        "title": 'Integration with ["Satellite imagery for select sudden onset major crisis events."](https://www.maxar.com/open-data/)',
    },
    "Algo: Semantic Segmentation": {
        "ICON": roofai_ICON,
        "url": "https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md",
        "marquee": "https://github.com/kamangir/assets/raw/main/palisades/prediction.png?raw=true",
        "title": "Integration with [segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch).",
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
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
