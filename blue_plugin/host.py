from typing import List

from abcli.host import signature as abcli_signature

from blue_plugin import fullname


def signature() -> List[str]:
    return [
        fullname(),
    ] + abcli_signature()
