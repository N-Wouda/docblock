def strip_doc(doc: str) -> str:
    """
    Strips a C-style documentation block of the opening and closing tags, and
    any continuation in multiline blocks. For example,
    ```
    /**
     * Test
     */
    ```
    is stripped to ``Test``.

    Parameters
    ----------
    doc
        The documentation block to strip.

    Returns
    -------
    str
        The stripped documentation block.
    """
    if doc == "/**/" or doc == "/***/":
        return ""

    lines = doc.splitlines()
    lines[0] = lines[0].replace("/**", "").replace("/*", "")
    lines[-1] = lines[-1].replace("*/", "")

    def clean(line):
        line = line.strip()
        if line.startswith("*"):
            line = line[2:] if line.startswith("* ") else line[1:]
        return line.rstrip()

    return "\n".join(map(clean, lines)).strip()
