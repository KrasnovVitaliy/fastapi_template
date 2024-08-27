from pydantic import BaseModel  # noqa: EXE002, D100


class TokenDataModel(BaseModel):
    """Defines a token model."""

    alg: str
    iss: str
    uid: int
    token_type: str
    iat: int
    exp: int
