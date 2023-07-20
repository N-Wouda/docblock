import pyparsing as pp

# Matches documentation blocks.
DOCBLOCK = pp.Combine(pp.Literal("/*") + ... + pp.Literal("*/"))

# Matches namespace declarations.
NAMESPACE = (
    pp.Suppress(pp.Keyword("namespace"))
    + pp.Word(pp.identbodychars)
    + pp.Supress("{")
)

# Matches class declarations.
CLASS = (
    pp.Suppress(pp.Keyword("class"))
    + pp.Word(pp.identbodychars)
    + pp.Supress("{")
)

# This could also match the class declaration, and then a whole bunch of stuff
# up to the first function. We do not want that, so there should *not* be a
# class keyword in front of the name.
FUNC = ~pp.Keyword("class") + pp.Word(pp.identbodychars) + pp.Suppress("(")

FUNCDOC = pp.Group(DOCBLOCK + ... + FUNC)
CLASSDOC = pp.Group(DOCBLOCK + ... + CLASS)
