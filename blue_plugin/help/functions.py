from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions

from blue_plugin import ALIAS
from blue_plugin.help.node.functions import help_functions as help_node


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions|repo"

    return show_usage(
        [
            "@plugin",
            "browse",
            f"[{options}]",
        ],
        "browse blue_plugin.",
        mono=mono,
    )


def help_leaf(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun,upload"
    args = [
        "[--<keyword-1> <value-1>]",
        "[--<keyword-2> <value-2>]",
    ]

    return show_usage(
        [
            "@plugin",
            "leaf",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "blue-plugin leaf <object-name>.",
        mono=mono,
    )


def help_task(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "<thing-1+thing-2>|all",
        ]
    )

    return show_usage(
        [
            "@plugin",
            "task",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "task -things-> <object-name>.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "browse": help_browse,
        "leaf": help_leaf,
        "node": help_node,
        "task": help_task,
    }
)
