from fastapi import FastAPI
from fastapi_pagination import add_pagination
import logging
from api.router import api_router

app = FastAPI(title="users-microservice")
add_pagination(app)
app.include_router(api_router, prefix="/api")
