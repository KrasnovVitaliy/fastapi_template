import logging

from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from models.bearer_auth import BearerAuthModel

logger = logging.getLogger(__name__)


def get_token_bearer_auth(
    authorization_credentials: HTTPAuthorizationCredentials,
) -> BearerAuthModel:
    logger.info("Received authorization credentials: %s", authorization_credentials)

    token_data = authorization_credentials.credentials
    # token_data = auth_token.read_access_token(access_token=authorization_credentials.credentials)
    if not token_data:
        logger.warning("Unknown access token: %s", authorization_credentials)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return BearerAuthModel(token_data=token_data, access_token=authorization_credentials.credentials)
