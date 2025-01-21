from typing import List

from blue_options.terminal import show_usage, xtra


def help_node(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@plugin",
            "node",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "blue-plugin node <object-name>.",
        mono=mono,
    )


def help_node_leaf(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)
    args = [
        "[--<keyword-1> <value-1>]",
        "[--<keyword-2> <value-2>]",
    ]

    return show_usage(
        [
            "@plugin",
            "node",
            "leaf",
            f"[{options}]",
            "[.|<object-name-1>]",
            "[-|<object-name-2>]",
        ]
        + args,
        "<object-name-1> -blue-plugin node leaf-> <object-name-2>.",
        mono=mono,
    )


help_functions = {
    "": help_node,
    "leaf": help_node_leaf,
}
