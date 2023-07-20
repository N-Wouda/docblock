# Docblock

[![PyPI version](https://badge.fury.io/py/docblock.svg)](https://badge.fury.io/py/docblock)
[![CI](https://github.com/N-Wouda/docblock/actions/workflows/CI.yaml/badge.svg?branch=main)](https://github.com/N-Wouda/docblock/actions/workflows/CI.yaml)
[![codecov](https://codecov.io/gh/N-Wouda/docblock/branch/main/graph/badge.svg?token=SWFVP2J84T)](https://codecov.io/gh/N-Wouda/docblock)

The `docblock` package reads and parses documentation from C and C++ header files. 
It is opinionated and explicitly does *not* cover all edge cases of the C (and especially not C++) grammar, but hopes to provide sufficient utility for most use cases.
The `docblock` package is a pure Python package and depends only on `pyparsing`.
It can be installed as
```shell
pip install docblock
``` 

## Example usage

TODO

## Why `docblock`?

Parsing documentation from header files is common practice to generate documentation.
One such tool is [pybind11_mkdoc](https://github.com/pybind/pybind11_mkdoc).
That tool, however, relies on clang and the LLVM project to parse C++ documentation blocks: great if you're already using clang, but very heavy-handed if you do not.

This is where `docblock` comes in: it is a pure Python package that does not aim to parse all of C and C++'s grammar, but only extracts the documentation block's content and the function point it documents.
Since `docblock` does not understand much of the underlying language, it will very likely not parse all documentation blocks correctly.
Feel free to open an issue if you have an example that is not parsed correctly.
