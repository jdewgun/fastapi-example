from fastapi import APIRouter

from app.api.v1.endpoints import health, meta, users

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(meta.router, tags=["meta"])
api_router.include_router(users.router, tags=["users"])
