// Simple namespace example. This tests if the documentation for test::Test and
// test::Test::test are parsed correctly.

namespace test
{
/**
 * Class documentation
 */
class Test
{
    /**
     * Test docstring
     */
    void test() const;

    /* Short one-line docstring. */
    void other();

    void noDocumentation();  // should not show up in parse result
};
};  // namespace test

namespace test::nested
{
/**
 * Nested class documentation.
 */
class Test;
};  // namespace test::nested
