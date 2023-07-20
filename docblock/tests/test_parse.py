from docblock import parse, parse_file


def test_parse_empty_string_returns_empty():
    assert parse("") == {}


def test_namespace():
    expected = {"test::Test::test": "Test docstring"}

    assert parse_file("docblock/tests/examples/namespace.h") == expected
