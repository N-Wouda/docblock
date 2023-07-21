from docblock.grammar import FUNC, ID, QUALIFIED_ID


def test_id_match():
    assert ID.matches("Value")
    assert ID.matches("value_123")
    assert ID.matches("Val2312")

    assert not ID.matches("@Exchange")
    assert not ID.matches("334#")
    assert not ID.matches("")
    assert not ID.matches(" ")


def test_qualified_id_match():
    assert QUALIFIED_ID.matches("pyvrp::Solution")
    assert QUALIFIED_ID.matches("::Solution")
    assert QUALIFIED_ID.matches("pyvrp::Solution::Route")


def test_func_match():
    assert FUNC.matches("DynamicBitset(std::vector<Block> data);")
    assert FUNC.matches("count() const;")
    assert FUNC.matches("Matrix(size_t nRows, size_t nCols);")
