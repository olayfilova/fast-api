from fastapi import APIRouter,status
from src.common.schemas.common import DetailsResponse


router=APIRouter()

@router.get(path="/health",
            tags=["health"],
            response_model=DetailsResponse,
            status_code=200
            )
def health_check()->DetailsResponse:
    """

    :return: Response: health status OK
    """
    return DetailsResponse(details="OK")
