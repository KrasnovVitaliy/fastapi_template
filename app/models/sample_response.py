from __future__ import annotations  # noqa: D100

from pydantic import BaseModel


class SampleResponseModel(BaseModel):
    """SampleResponseModel - sample response model for demo only.

    code: The code of this ApiResponse [Optional].
    message: The message of this ApiResponse [Optional].
    """

    code: int | None = None
    message: str | None = None
