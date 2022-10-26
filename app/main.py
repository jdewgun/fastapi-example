from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.api.router import api_router
from typing import Dict
import logging

app = FastAPI(title="users-microservice")
add_pagination(app)
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root() -> Dict:
    return {"message": "Welcome to the Users Microservice."}
