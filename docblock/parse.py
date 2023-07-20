import pathlib
from collections import defaultdict
from typing import Dict, List, Union

from docblock.grammar import (
    CLASS,
    DOCBLOCK,
    FUNC,
    ITEMS,
    LBRACE,
    NAMESPACE,
    RBRACE,
)

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
    result: _ParsedType = defaultdict(list)
    namespace = []
    last_id = None
    docblock = None

    for match, start, end in ITEMS.scan_string(code):
        segment = code[start:end]
        name = match[-1]

        if any(item.matches(segment) for item in [NAMESPACE, CLASS, FUNC]):
            last_id = name

            if docblock is not None:
                where = "::".join([*namespace, last_id])
                result[where].append(docblock)
                docblock = None

        if LBRACE.matches(segment):
            namespace.append(last_id)

        if RBRACE.matches(segment):
            namespace.pop()

        if DOCBLOCK.matches(segment):
            docblock = name

    return result
