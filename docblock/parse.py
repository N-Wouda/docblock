import pathlib
from typing import Union


def parse(code: str):
    """
    TODO
    """
    pass


def parse_file(loc: Union[pathlib.Path, str]):
    """
    TODO
    """
    with open(loc, "r") as fh:
        code = fh.read()

    return parse(code)
