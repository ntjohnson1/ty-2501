from __future__ import annotations

import warnings
from collections.abc import Sequence
from typing import TYPE_CHECKING

import numpy as np
import numpy.typing as npt

if TYPE_CHECKING:
    from . import Rgba32ArrayLike, Rgba32Like


class Rgba32Ext:
    """Extension for [Rgba32][rerun.datatypes.Rgba32]."""

    """
    Extension for the `Rgba32` datatype.

    Possible input for `Rgba32`:
    - Sequence[int]: interpreted as rgb or rgba values in 0-255 range
    - numpy array: interpreted as rgb or rgba values, range depending on dtype
    - anything else (int or convertible to int): interpreted as a 32-bit packed rgba value

    Possible inputs for `Rgba32Batch()`:
    - a single `Rgba32` instance
    - a sequence of `Rgba32` instances
    - Nx3 or Nx4 numpy array, range depending on dtype
    """

    @staticmethod
    def rgba__field_converter_override(data: Rgba32Like) -> int:
        from . import Rgba32

        if isinstance(data, Rgba32):
            return int(0)
        if isinstance(data, np.ndarray):
            return int(1)
        elif isinstance(data, Sequence):
            data = np.array(data).reshape((1, -1))
            if data.shape[1] not in (3, 4):
                raise ValueError(f"expected sequence of length of 3 or 4, received {data.shape[1]}")
            return int(0)
        else:
            return int(data)

