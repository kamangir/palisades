import os
import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from palisades import NAME
from palisades.workflow.ingest import generate_ingest_workflow
from palisades.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "generate"


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--workflow_name",
    type=str,
)
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--query_object_name",
    type=str,
)
parser.add_argument(
    "--count",
    type=int,
)
parser.add_argument(
    "--do_tag",
    type=int,
)
parser.add_argument(
    "--datacube_ingest_options",
    type=str,
)
parser.add_argument(
    "--predict_options",
    type=str,
)
parser.add_argument(
    "--model_object_name",
    type=str,
)
parser.add_argument(
    "--buildings_query_options",
    type=str,
)
parser.add_argument(
    "--analysis_options",
    type=str,
)
args = parser.parse_args()

success = args.task in list_of_tasks
if args.task == "generate":
    if args.workflow_name == "ingest":
        success = generate_ingest_workflow(
            job_name=args.job_name,
            query_object_name=args.query_object_name,
            count=args.count,
            do_tag=args.do_tag == 1,
            datacube_ingest_options=args.datacube_ingest_options,
            predict_options=args.predict_options,
            model_object_name=args.model_object_name,
            buildings_query_options=args.buildings_query_options,
            analysis_options=args.analysis_options,
        )
    else:
        success = False
        logger.error("{}: workflow not found.")
else:
    success = None

sys_exit(logger, NAME, args.task, success)
