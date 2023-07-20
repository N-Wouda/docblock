import pathlib
from collections import defaultdict
from typing import Dict, List, Union

from docblock.grammar import (
    CLASS,
    DOCBLOCK,
    FUNC,
    LBRACE,
    NAMESPACE,
    RBRACE,
    SYNTAX,
)
from docblock.utils import strip_doc

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
        (values) that were encountered. In case of overloads, there may be
        multiple documentation blocks for the same functional end point.
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
        (values) that were encountered. In case of overloads, there may be
        multiple documentation blocks for the same functional end point.
    """
    result: _ParsedType = defaultdict(list)
    namespace = []
    last_id = None
    docblock = None

    for match, start, end in SYNTAX.scan_string(code):
        assert len(match) == 1

        parsed = match[0]
        raw = code[start:end]

        if any(matcher.matches(raw) for matcher in [NAMESPACE, CLASS, FUNC]):
            last_id = parsed

            if docblock is not None:
                where = "::".join([*namespace, last_id])
                result[where].append(docblock)
                docblock = None

        if LBRACE.matches(raw):
            namespace.append(last_id)

        if RBRACE.matches(raw):
            namespace.pop()

        if DOCBLOCK.matches(raw):
            docblock = strip_doc(parsed)

    return result
