from docblock import parse


def test_parse_empty_string_returns_empty():
    assert parse("") == {}
