import pyparsing as pp

ID = pp.Word(pp.identbodychars)
QUALIFIED_ID = pp.Combine(pp.OneOrMore(pp.Optional(ID + "::") + ID))

LPAR, RPAR = pp.Literal("("), pp.Literal(")")
LBRACE, RBRACE = pp.Literal("{"), pp.Literal("}")
CLOSE_STMT = pp.Literal(";")

NAMESPACE = pp.Keyword("namespace") + QUALIFIED_ID
CLASS = (pp.Keyword("struct") | pp.Keyword("class")) + QUALIFIED_ID
FUNC = QUALIFIED_ID + (LPAR + ... + CLOSE_STMT).suppress()

DOCBLOCK = pp.Combine(pp.Literal("/*") + ... + pp.Literal("*/"))
COMMENT = pp.Literal("//") + pp.rest_of_line

ITEMS = (NAMESPACE | CLASS | FUNC | LBRACE | RBRACE | DOCBLOCK).ignore(COMMENT)
