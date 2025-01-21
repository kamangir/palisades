import os

from blue_objects import file, README
from blue_geo import ICON as blue_geo_ICON
from roofai import ICON as roofai_ICON

from palisades import NAME, VERSION, ICON, REPO_NAME

# refactor

list_of_menu_item = {
    "Maxar Open Data": {
        "ICON": blue_geo_ICON,
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data",
        "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true",
        "title": 'Source of ["Satellite imagery for select sudden onset major crisis events."](https://www.maxar.com/open-data/)',
    },
    "Step by Step Review": {
        "ICON": ICON,
        "url": "#",
        "marquee": "",
        "title": "",
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
