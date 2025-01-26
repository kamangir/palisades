from typing import Dict, Any
from tqdm import tqdm

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.metadata import post_to_object
from blue_objects.mlflow.tags import create_filter_string
from blue_objects.storage import instance as storage

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def ingest_analytics(
    object_name: str,
    acq_count: int = -1,
    building_count: int = -1,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest_analytics -{}{}> {}".format(
            NAME,
            f"{acq_count} acq(s)-" if acq_count != -1 else "",
            f"{building_count} buildings(s)-" if building_count != -1 else "",
            object_name,
        )
    )

    list_of_prediction_objects = mlflow.search(
        create_filter_string("contains=palisades.prediction,profile=FULL")
    )
    if acq_count != -1:
        list_of_prediction_objects = list_of_prediction_objects[:acq_count]
    logger.info(f"{len(list_of_prediction_objects)} acq(s) to process.")

    metadata: Dict[str, Any] = {"ingested": {}}
    success_count: int = 0
    for prediction_object_name in tqdm(list_of_prediction_objects):
        logger.info(f"processing {prediction_object_name} ...")

        metadata["ingested"][prediction_object_name] = False

        if not storage.exists(f"{prediction_object_name}/analysis.gpkg"):
            logger.warning("analysis.gkpg not found.")
            continue

        if not storage.download_file(
            object_name=f"bolt/{prediction_object_name}/analysis.gpkg",
            filename="object",
            log=verbose,
        ):
            continue

        if not file.copy(
            objects.path_of(
                "analysis.gpkg",
                prediction_object_name,
            ),
            objects.path_of(
                f"analysis-{prediction_object_name}.gpkg",
                object_name,
            ),
            log=verbose,
        ):
            continue

        metadata["ingested"][prediction_object_name] = True
        success_count += 1

    logger.info(
        "processed {} object(s), ingested {} successfully.".format(
            len(metadata["ingested"]),
            success_count,
        )
    )

    return post_to_object(
        object_name,
        "analytics.ingest",
        metadata,
    )
