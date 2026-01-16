from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from . import Rgba32Like


class Rgba32Ext:
    @staticmethod
    def converter(data: Rgba32Like) -> int:
        if isinstance(data, Sequence):
            data = np.array(data).reshape((1, -1))
            if data.shape[1] not in (3, 4):
                raise ValueError(f"expected sequence of length of 3 or 4, received {data.shape[1]}")
            return int(0)
        return int(1)

