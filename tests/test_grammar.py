from docblock.grammar import CLASS, FUNC, ID, OPERATOR, QUALIFIED_ID


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
    # Basic function declarations: one name, some parens, and a semicolon.
    assert FUNC.matches("DynamicBitset(std::vector<Block> data);")
    assert FUNC.matches("count() const;")
    assert FUNC.matches("Matrix(size_t nRows, size_t nCols);")

    assert FUNC.matches("bpd(Solution const &first, Solution const &second);")

    # These are a bit harder, because the name is hard, or because there are
    # multiple parentheses.
    assert FUNC.matches("operator()(size_t row, size_t col);")
    assert FUNC.matches("operator|(pyvrp::DynamicBitset const &other) const;")
    assert FUNC.matches("operator~() const;")

    # Both orderings (const override, and override const) should be accepted.
    assert FUNC.matches("apply(Node *U, Node *V) const override;")
    assert FUNC.matches("apply(Node *U, Node *V) override const;")


def test_func_matches_complicated():
    assert FUNC.matches(
        """
        timeWarp(Duration const maxDuration
                 = std::numeric_limits<Duration>::max()) const;
        """
    )

    assert FUNC.matches(
        """
        timeWarp(Duration const maxDuration
                 = std::numeric_limits<Duration>::max(),
                 Duration const maxOvertime = 0) const;
        """
    )

    assert not FUNC.matches(
        """
        operator[](size_t idx) const
        {
            auto const q = idx / BLOCK_SIZE;
        """
    )


def test_operator_match():
    assert OPERATOR.matches("operator~")
    assert OPERATOR.matches("operator|")
    assert OPERATOR.matches("operator||")
    assert OPERATOR.matches("operator()")
    assert OPERATOR.matches("operator[]")
    assert OPERATOR.matches("operator<=>")

    assert not OPERATOR.matches("operator(")
    assert not OPERATOR.matches("operator|(")
    assert not OPERATOR.matches("operator()(")


def test_class_match():
    # Basic classes and struct definitions.
    assert CLASS.matches("class Route")
    assert CLASS.matches("struct Route")

    # A bit harder, due to the alignment in between.
    assert CLASS.matches("struct alignas(16) Route")
