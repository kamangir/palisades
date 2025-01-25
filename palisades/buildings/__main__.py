import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from palisades import NAME
from palisades import env
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
parser.add_argument(
    "--buffer",
    type=float,
    default=env.PALISADES_DEFAULT_BUFFER_M,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--max_count",
    type=int,
    default=-1,
    help="-1: all",
)

args = parser.parse_args()

success = False
if args.task == "analyze":
    success = analyze_buildings(
        object_name=args.object_name,
        buffer=args.buffer,
        verbose=args.verbose == 1,
        max_count=args.max_count,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
