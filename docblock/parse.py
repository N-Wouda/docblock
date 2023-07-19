import pathlib
from typing import Dict, List, Union

_ParsedType = Dict[str, List]


def parse(code: str) -> _ParsedType:
    """
    TODO
    """
    return {}


def parse_file(loc: Union[pathlib.Path, str]):
    """
    TODO
    """
    with open(loc, "r") as fh:
        code = fh.read()

    return parse(code)
