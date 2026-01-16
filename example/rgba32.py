from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

import numpy as np
import numpy.typing as npt

from .rgba32_ext import Rgba32Ext

__all__ = ["Rgba32", "Rgba32ArrayLike", "Rgba32Like"]


class Rgba32(Rgba32Ext):

    def __init__(self: Any, rgba: Rgba32Like) -> None:
        pass

if TYPE_CHECKING:
    Rgba32Like = Rgba32 | int | Sequence[int | float] | npt.NDArray[np.uint8 | np.float32 | np.float64]
    """A type alias for any Rgba32-like object."""
else:
    Rgba32Like = Any

Rgba32ArrayLike = Rgba32 | Sequence[Rgba32Like] | int | npt.ArrayLike
"""A type alias for any Rgba32-like array object."""

