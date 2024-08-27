from __future__ import annotations  # noqa: D100

from abc import ABCMeta, abstractmethod


class SampleStoreABC:
    """Sample store."""

    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_data(self, user_id: int) -> int:
        """Get data from a store."""
