from blueness import module

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def render_analytics(
    object_name: str,
    building_id: str,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.render_analytics: {} @ {}".format(
            NAME,
            building_id,
            object_name,
        )
    )

    logger.info("🪄")

    return True
