from __future__ import annotations  # noqa: D100

from pydantic import BaseModel


class SampleRequestModel(BaseModel):
    """Sample request body model."""

    user_id: int  # User id
