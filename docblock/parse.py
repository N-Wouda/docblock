import pathlib
from typing import Dict, List, Union

_ParsedType = Dict[str, List[str]]


def parse_file(loc: Union[pathlib.Path, str]) -> _ParsedType:
    """
    Parses a header file at the given location. See ``parse`` for details.

    Parameters
    ----------
    loc
        Location of the header file. Must be either a path or a string
        representing a path.

    Returns
    -------
    dict
        A dictionary of functional end point (keys) to documentation blocks
        (values) that were encountered. There may be multiple documentation
        blocks for the same functional end point in case of overloads.
    """
    with open(loc, "r") as fh:
        code = fh.read()

    return parse(code)


def parse(code: str) -> _ParsedType:
    """
    Parses the given string for documentation blocks.

    Parameters
    ----------
    code
        Raw, unparsed source code.

    Returns
    -------
    dict
        A dictionary of functional end point (keys) to documentation blocks
        (values) that were encountered. There may be multiple documentation
        blocks for the same functional end point in case of overloads.
    """
    return {}  # TODO
