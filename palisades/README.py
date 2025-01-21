import os

from blue_objects import file, README

from palisades import NAME, VERSION, ICON, REPO_NAME

# refactor

list_of_menu_item = {
    "Maxar Open Data": {
        "ICON": ICON,
        "url": "#",
        "marquee": "",
        "title": "",
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
