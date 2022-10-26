import logging
from typing import Dict

from fastapi import APIRouter

from app.api.v1.schemas.meta import Meta

logger = logging.getLogger(name="__main__")
router = APIRouter()


@router.get("/meta", status_code=200)
@router.get("/meta/", status_code=200)
async def meta() -> Dict:
    logger.info("Meta Endpoint called.")
    return {"meta": Meta(app_version="0.1.0"), "error": {}}
