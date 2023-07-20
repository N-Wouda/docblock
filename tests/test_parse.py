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


def test_example_CostEvaluator():
    """
    Test a real-world example for PyVRP.
    """
    expected = {
        "pyvrp::CostEvaluator": [
            "Cost evaluator class that computes penalty values for timewarp "
            "and load."
        ],
        "pyvrp::CostEvaluator::loadPenalty": [
            "Computes the total excess capacity penalty for the given load."
        ],
        "pyvrp::CostEvaluator::loadPenaltyExcess": [
            "Computes the excess capacity penalty for the given excess load, "
            "that is,\nthe part of the load that exceeds the capacity."
        ],
        "pyvrp::CostEvaluator::twPenalty": [
            "Computes the time warp penalty for the given time warp."
        ],
        "pyvrp::CostEvaluator::penalisedCost": [
            "Computes a smoothed objective (penalised cost) for a given "
            "solution."
        ],
        "pyvrp::CostEvaluator::cost": [
            "Computes the objective for a given solution. Returns the "
            "largest\nrepresentable cost value if the solution is infeasible."
        ],
    }

    assert parse_file("tests/examples/CostEvaluator.h") == expected


def test_example_readme():
    expected = {
        "test": ["Test namespace."],
        "test::Test::Test": ["First constructor", "Second constructor"],
        "test::Test::aMethod": ["A method."],
    }

    assert parse_file("tests/examples/readme.h") == expected


def test_example_diversity():
    expected = {
        "pyvrp::diversity::brokenPairsDistance": [
            "Parameters\n"
            "----------\n"
            "first\n"
            "    First solution.\n"
            "second\n"
            "    Second solution."
        ]
    }

    assert parse_file("tests/examples/diversity.h") == expected
