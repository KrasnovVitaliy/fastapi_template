from __future__ import annotations  # noqa: D100

from store.sample_store_abc import SampleStoreABC


class InmemorySampleStore(SampleStoreABC):
    """Inmemory sample store."""

    async def get_data(self, user_id: int) -> int:  # noqa: D102
        return user_id
