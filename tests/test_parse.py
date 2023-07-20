from docblock.parse import parse, parse_file


def test_parse_empty_string_returns_empty():
    assert parse("") == {}


def test_example_namespace():
    expected = {
        "test::Test": ["Class documentation"],
        "test::Test::test": ["Test docstring"],
        "test::Test::other": ["Short one-line docstring."],
        "test::nested::Test": ["Nested class documentation."],
    }

    assert parse_file("tests/examples/namespace.h") == expected


def test_example_multiline():
    parts = [
        "This is a multiline docstring.\n",
        "It contains multiple lines, and punctuation; and numbers like 1, 2",
        "and ends abruptly.\n",
        "Like so.",
    ]

    expected = {"Test::test": ["\n".join(parts)]}
    assert parse_file("tests/examples/multiline.h") == expected


def test_example_overload():
    expected = {
        "test": [
            "This function takes a single argument.",
            "This function takes two arguments.",
            "This function takes three arguments.",
        ]
    }

    assert parse_file("tests/examples/overload.h") == expected
