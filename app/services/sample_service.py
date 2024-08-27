from __future__ import annotations  # noqa: D100

import logging

from models.sample_request import SampleRequestModel  # noqa: TCH002
from models.sample_response import SampleResponseModel  # noqa: TCH002
from store.sample_store_abc import SampleStoreABC  # noqa: TCH002

logger = logging.getLogger(__name__)


class SampleService:
    """Sample service."""

    def __init__(self, sample_store: SampleStoreABC) -> None:  # noqa: D107
        self.sample_store = sample_store

    async def sample_post(self, body: SampleRequestModel) -> SampleResponseModel:
        """Sample post handler.

        Args:
        ----
            body (SampleRequestModel): Request body

        Returns:
        -------
            SampleResponseModel: Response

        """
        logger.debug("Received request body: %s", body)
        db_data = self.sample_store.get_data(user_id=body.user_id)
        return SampleResponseModel(code=db_data, message="Response")
