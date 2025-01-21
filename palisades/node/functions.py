from blueness import module
from palisades import NAME
from palisades.logger import logger


NAME = module.name(__file__, NAME)


def func(arg: str) -> bool:
    logger.info(f"{NAME}.func: arg={arg}")
    return True


