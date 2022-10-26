import logging
from typing import Dict

from fastapi import APIRouter

logger = logging.getLogger(name="__main__")
router = APIRouter()


@router.get("/health", status_code=200)
@router.get("/health/", status_code=200)
async def health() -> Dict:
    logger.info("Health Endpoint called.")
    return {"health": "stable", "error": {}}
