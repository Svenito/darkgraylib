"""Common helpers used by `darker.__main__` and `graylint.__main__`"""

from pathlib import Path
from typing import List, Optional, Set, Tuple

from darkgraylib.utils import get_common_root


def resolve_paths(
    stdin_filename: Optional[str], src: List[str]
) -> Tuple[Set[Path], Path]:
    """Resolve paths from the ``src`` and ``--stdin-filename`` command line arguments

    :param stdin_filename: The value of the ``--stdin-filename`` command line argument,
                           or ``None`` if the option was not given
    :param src: The value of the ``src`` command line argument
    :return: A tuple of the resolved paths and the common root directory of the paths

    """
    if stdin_filename is not None:
        paths = {Path(stdin_filename)}
        # `parse_command_line` guarantees that `args.src` is empty
    else:
        paths = {Path(p) for p in src}
        # `parse_command_line` guarantees that `args.stdin_filename` is `None`
    return paths, get_common_root(paths)
