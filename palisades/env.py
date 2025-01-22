import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


PALISADES_SECRET = os.getenv(
    "PALISADES_SECRET",
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

PALISADES_DEFAULT_FIRE_MODEL = os.getenv(
    "PALISADES_DEFAULT_FIRE_MODEL",
    "",
)

PALISADES_QGIS_TEMPLATE_PREDICT = os.getenv(
    "PALISADES_QGIS_TEMPLATE_PREDICT",
    "",
)
