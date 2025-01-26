from blueness import module

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

    logger.info("🪄")

    return True
