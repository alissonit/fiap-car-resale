from fastapi import APIRouter, Depends
from typing import Annotated

from src.configuration.settings import DBSettings, get_db_settings

router = APIRouter(prefix="/v1")


@router.get("/settings", response_model=DBSettings)
async def get_settings(
    db_settings: Annotated[DBSettings, Depends(
        get_db_settings)]) -> DBSettings:
    """
    Get settings
    """
    return db_settings
