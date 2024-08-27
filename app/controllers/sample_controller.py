from fastapi import (  # noqa: D100
    APIRouter,
    Body,
    HTTPException,
    Query,
    Request,
    status,
)
from models.sample_request import SampleRequestModel
from models.sample_response import SampleResponseModel

router = APIRouter()


@router.post(
    "/sample/",
    responses={
        200: {"model": SampleResponseModel, "description": "successful operation"},
        400: {"description": "Invalid request data"},
        404: {"description": "Data not found"},
    },
    tags=["sample"],
    summary="Sample controller endpoint",
)
async def sample_post(
    request: Request,
    phone: str = Query(None, description="User phone"),
    body: SampleRequestModel = Body(None, description="Sample request body"),  # noqa: B008
) -> SampleResponseModel:
    if body.user_id == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not validate request data",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return request.app.state.sample_service.sample_post(body)
