import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


BLUE_PLUGIN_SECRET = os.getenv(
    "BLUE_PLUGIN_SECRET",
    "",
)

BLUE_PLUGIN_CONFIG = os.getenv(
    "BLUE_PLUGIN_CONFIG",
    "",
)
