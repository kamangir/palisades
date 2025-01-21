from typing import List

from abcli.host import signature as abcli_signature
from blue_geo import fullname as blue_geo_fullname
from roofai import fullname as roofai_fullname

from palisades import fullname


def signature() -> List[str]:
    return [
        fullname(),
        blue_geo_fullname(),
        roofai_fullname(),
    ] + abcli_signature()
