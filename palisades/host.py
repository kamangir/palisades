from typing import List

from abcli.host import signature as abcli_signature

from palisades import fullname


def signature() -> List[str]:
    return [
        fullname(),
    ] + abcli_signature()
