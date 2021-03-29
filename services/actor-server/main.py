from fastapi import FastAPI
from actor import actor
import uvicorn

app = FastAPI()

app.include_router(actor)
