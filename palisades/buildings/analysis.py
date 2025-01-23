from blueness import module

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def analyze_buildings(object_name: str) -> bool:
    logger.info(
        "{}.analyze_buildings({})".format(
            NAME,
            object_name,
        )
    )

    logger.info("🪄")

    return True
