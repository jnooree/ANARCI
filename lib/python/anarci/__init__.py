from importlib.metadata import PackageNotFoundError, version

from . import anarci, schemes

__all__ = ["anarci", "schemes"]

try:
    __version__ = version("ANARCI")
except PackageNotFoundError:
    pass

del PackageNotFoundError, version
