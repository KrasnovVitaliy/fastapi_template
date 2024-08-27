from fastapi import Depends  # noqa: D100
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows  # noqa: F401
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from models.extra_models import TokenModel
from services import security_impl

bearer_auth = HTTPBearer()


def get_token_bearer_auth(credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> TokenModel:
    """Check and retrieve authentication information from custom bearer token.

    :param credentials Credentials provided by Authorization header
    :type credentials: HTTPAuthorizationCredentials
    :return: Decoded token information or None if token is invalid
    :rtype: TokenModel | None
    """
    return security_impl.get_token_bearer_auth(credentials)
