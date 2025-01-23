import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from palisades import NAME
from palisades.buildings.analysis import analyze_buildings
from palisades.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="analyze",
)
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "analyze":
    success = analyze_buildings(
        object_name=args.object_name,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
