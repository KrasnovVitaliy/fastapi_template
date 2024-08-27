from models.token_data import TokenDataModel  # noqa: EXE002, D100
from pydantic import BaseModel


class BearerAuthModel(BaseModel):
    """Data stored in a refresh token record."""

    token_data: TokenDataModel
    access_token: str
