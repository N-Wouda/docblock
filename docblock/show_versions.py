import sys
from importlib.metadata import version


def show_versions():
    """
    This function prints version information that is useful when filing bug
    reports.

    Examples
    --------
    Calling this function should print information like the following
    (dependency versions in your local installation will likely differ):

    >>> import docblock
    >>> docblock.show_versions()
    INSTALLED VERSIONS
    ------------------
     docblock: 0.0.1
    pyparsing: 3.1.0
       Python: 3.9.9
    """
    python_version = ".".join(map(str, sys.version_info[:3]))

    print("INSTALLED VERSIONS")
    print("------------------")
    print(f" docblock: {version('docblock')}")
    print(f"pyparsing: {version('pyparsing')}")
    print(f"   Python: {python_version}")
