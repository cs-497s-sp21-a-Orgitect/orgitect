from fastapi import FastAPI
from app.api.actor import actor
from fastapi.staticfiles import StaticFiles
from app.api.db import metadata, database, engine

import uvicorn

metadata.create_all(engine)

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(actor,prefix='/api/v1/actor', tags=['actor'])
