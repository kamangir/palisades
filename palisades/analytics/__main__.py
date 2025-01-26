import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from palisades import NAME
from palisades.analytics.ingest import ingest_analytics
from palisades.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="ingest",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--acq_count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--building_count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "ingest":
    success = ingest_analytics(
        object_name=args.object_name,
        acq_count=args.acq_count,
        building_count=args.building_count,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
