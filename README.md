[![PyPI version](https://badge.fury.io/py/docblock.svg)](https://badge.fury.io/py/docblock)
[![CI](https://github.com/N-Wouda/docblock/actions/workflows/CI.yaml/badge.svg?branch=main)](https://github.com/N-Wouda/docblock/actions/workflows/CI.yaml)
[![codecov](https://codecov.io/gh/N-Wouda/docblock/branch/main/graph/badge.svg?token=SWFVP2J84T)](https://codecov.io/gh/N-Wouda/docblock)

The `docblock` package reads and parses documentation from C++ header files.
It should also work out of the box for C header files, but that is currently untested.
It is opinionated and explicitly does *not* cover all edge cases of the C++ grammar, but hopes to provide sufficient utility for most use cases.
The package assumes documentation blocks are formatted using C-style comments, as follows:
```cpp
/**
 * Text
 */
void func();
```
That is, the documentation block starts with `/*` or `/**`, and ends with `*/`.
Any starting `*` on documentation lines in the block are allowed, but not required.
> To avoid parsing issues, non-documentation block comments SHOULD NOT use C-style comments. 

The `docblock` package is a pure Python package and depends only on `pyparsing`.
It can be installed as
```shell
pip install docblock
``` 

## Example usage

TODO

## Why `docblock`?

Parsing documentation from header files is common practice to generate documentation, particularly in mixed-language projects where the C++ components are intended to be used from another language.
One tool that simplifies this for C++-to-Python is [pybind11_mkdoc](https://github.com/pybind/pybind11_mkdoc).
That tool, however, relies on clang and the LLVM project to parse C++ documentation blocks: great if you're already using clang, but very heavy-handed if you do not.

This is where `docblock` comes in: it is a pure Python package that does not aim to parse all of C++'s grammar, but only extracts the documentation block's content and the function point it documents.
That is far easier to implement (not requiring a full compiler), but does mean it will very likely not parse all documentation blocks correctly.
Feel free to open an issue if you have an example that is not parsed correctly by `docblock`.
