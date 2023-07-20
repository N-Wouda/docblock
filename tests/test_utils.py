from docblock.utils import strip_doc


def test_strip_open_close_tags():
    assert strip_doc("/**/") == ""
    assert strip_doc("/***/") == ""

    assert strip_doc("/** test */") == "test"
    assert strip_doc("/* test */") == "test"


def test_strip_whitespace_and_star():
    assert strip_doc("/**   * test\n  * test */") == "test\ntest"
    assert strip_doc("/* * test\n * test\n **test */") == "test\ntest\n*test"


def test_strip_newlines():
    comment = "/**\n * Nested class documentation.\n */"
    expected = "Nested class documentation."
    assert strip_doc(comment) == expected
