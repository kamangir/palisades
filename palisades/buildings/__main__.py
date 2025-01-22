import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="task",
)
args = parser.parse_args()

success = False
if args.task == "task":
    success = False
else:
    success = None

sys_exit(logger, NAME, args.task, success)
