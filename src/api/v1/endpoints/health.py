from fastapi import APIRouter
from typing import Dict
import logging

logger = logging.getLogger(name="__main__")
router = APIRouter()


@router.get("/health", status_code=200)
@router.get("/health/", status_code=200)
async def health() -> Dict:
    logger.info("Health Endpoint called.")
    return {"health": "stable", "error": {}}
