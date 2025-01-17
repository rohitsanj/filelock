"""Async implementation of filelock."""
from __future__ import annotations

import sys
import warnings
from typing import TYPE_CHECKING

from ._api import AsyncAcquireReturnProxy, BaseFileLock
from ._error import Timeout
from ._soft import SoftFileLock
from ._unix import UnixFileLock, has_fcntl
from ._windows import WindowsFileLock

if sys.platform == "win32":  # pragma: win32 cover
    _FileLock: type[BaseFileLock] = WindowsFileLock
else:  # pragma: win32 no cover # noqa: PLR5501
    if has_fcntl:
        _FileLock: type[BaseFileLock] = UnixFileLock
    else:
        _FileLock = SoftFileLock
        if warnings is not None:
            warnings.warn("only soft file lock is available", stacklevel=2)

if TYPE_CHECKING:  # noqa: SIM108
    FileLock = SoftFileLock
else:
    #: Alias for the lock, which should be used for the current platform.
    FileLock = _FileLock


__all__ = [
    "FileLock",
    "SoftFileLock",
    "Timeout",
    "UnixFileLock",
    "WindowsFileLock",
    "BaseFileLock",
    "AsyncAcquireReturnProxy",
]
