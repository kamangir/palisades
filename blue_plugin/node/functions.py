from blueness import module
from blue_plugin import NAME
from blue_plugin.logger import logger


NAME = module.name(__file__, NAME)


def func(arg: str) -> bool:
    logger.info(f"{NAME}.func: arg={arg}")
    return True
