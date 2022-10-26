import logging
from typing import Dict

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.router import api_router
from app.models.base import Base, engine

logger = logging.getLogger("__main__")

app = FastAPI(title="users-microservice")
add_pagination(app)
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def create_db_tables(db_engine=engine):
    Base.metadata.create_all(bind=db_engine)


@app.on_event("shutdown")
async def drop_db_tables(db_engine=engine):
    Base.metadata.drop_all(bind=db_engine)


@app.get("/")
async def root() -> Dict:
    return {"message": "Welcome to the Users Microservice."}
