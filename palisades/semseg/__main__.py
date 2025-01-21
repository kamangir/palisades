import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from roofai.semseg import Profile

from palisades import NAME
from palisades.semseg.predict import predict
from palisades.logger import logger

NAME = module.name(__file__, NAME)


list_of_tasks = "predict"

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--datacube_id",
    type=str,
)
parser.add_argument(
    "--device",
    type=str,
    default="cpu",
    help="cpu|cuda",
)
parser.add_argument(
    "--model_object_name",
    type=str,
)
parser.add_argument(
    "--prediction_object_name",
    type=str,
)
parser.add_argument(
    "--profile",
    type=str,
    default="VALIDATION",
    help="FULL|QUICK|VALIDATION",
)
args = parser.parse_args()

success = False
if args.task == "predict":
    success = predict(
        model_object_name=args.model_object_name,
        datacube_id=args.datacube_id,
        prediction_object_name=args.prediction_object_name,
        device=args.device,
        profile=Profile[args.profile],
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
