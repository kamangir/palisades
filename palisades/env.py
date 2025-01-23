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

PALISADES_TEST_PREDICTION_OBJECT = os.getenv(
    "PALISADES_TEST_PREDICTION_OBJECT",
    "",
)

PALISADES_DEFAULT_BUFFER_M_str = os.getenv(
    "PALISADES_DEFAULT_BUFFER_M",
    "",
)
try:
    PALISADES_DEFAULT_BUFFER_M = float(PALISADES_DEFAULT_BUFFER_M_str)
except Exception:
    PALISADES_DEFAULT_BUFFER_M = 50
