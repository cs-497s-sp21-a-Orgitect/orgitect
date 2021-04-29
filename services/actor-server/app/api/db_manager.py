from app.api.model import ActorIn, ActorOut, ActorUpdate
from app.api.db import actor, database

#handles database request/response
async def add_actor(payload: ActorIn):
    query = actor.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_actor():
    query = actor.select()
    return await database.fetch_all(query=query)

async def get_actor(id):
    query = actor.select(actor.c.id==id)
    c=await database.fetch_one(query=query)
    print(c)
    return c

async def delete_actor(id: int):
    query = actor.delete().where(actor.c.id==id)
    return await database.execute(query=query)

async def update_actor(id: int, payload: ActorIn):
    query = (
        actor
        .update()
        .where(actor.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)