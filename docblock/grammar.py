import pyparsing as pp

# Names in C++ can either be standalone, or fully qualified parts of a
# namespace. In the latter case the name consists of multiple parts separated
# by "::".
ID = pp.Word(pp.identbodychars)
QUALIFIED_ID = pp.Combine(pp.OneOrMore(pp.Optional("::") + ID))

LPAR, RPAR = pp.Literal("("), pp.Literal(")")
LBRACE, RBRACE = pp.Literal("{"), pp.Literal("}")
CLOSE_STMT = pp.Literal(";")

# Namespace, class (struct) and function definitions. These are fairly crude
# but seem to work well.
NAMESPACE = pp.Keyword("namespace").suppress() + QUALIFIED_ID
CLASS = (pp.Keyword("struct") | pp.Keyword("class")).suppress() + QUALIFIED_ID

# Exclude braces: we only want the delcarations, not any implementations.
# Assumes those are separated. Some special care is needed to match
# "operator X" overloads.
OPERATOR = "operator" + (pp.Word("<>!=&|*/+-~^", min=1, max=3) | "()" | "[]")
FUNC_NAME = OPERATOR | QUALIFIED_ID
FUNC = FUNC_NAME + (LPAR + ... + RPAR + ID[...] + CLOSE_STMT).suppress()

# Line comment and documentation blocks.
LINE_COMMENT = pp.dbl_slash_comment
DOCBLOCK = pp.c_style_comment

# Complete syntax we match on, ignoring (end-of-)line comments.
_ITEMS = NAMESPACE | CLASS | FUNC | LBRACE | RBRACE | DOCBLOCK
SYNTAX = _ITEMS.ignore(LINE_COMMENT)
