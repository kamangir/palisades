import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


BLUE_PLUGIN_SECRET = os.getenv(
    "BLUE_PLUGIN_SECRET",
    "",
)

PALISADES_QUERY_OBJECT_PALISADES_MAXAR = os.getenv(
    "PALISADES_QUERY_OBJECT_PALISADES_MAXAR",
    "",
)

PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST = os.getenv(
    "PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST",
    "",
)
