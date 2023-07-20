def strip_doc(comment: str) -> str:
    """
    TODO
    """
    if comment == "/**/" or comment == "/***/":
        return ""

    lines = comment.splitlines()
    lines[0] = lines[0].replace("/**", "").replace("/*", "")
    lines[-1] = lines[-1].replace("*/", "")

    def clean(line):
        line = line.strip()
        if line.startswith("*"):
            line = line[1:]
        return line.strip()

    return "\n".join(map(clean, lines)).strip()
