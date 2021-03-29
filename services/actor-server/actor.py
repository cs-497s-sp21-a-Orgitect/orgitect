from fastapi import Header, APIRouter,HTTPException
from pydantic import BaseModel
from typing import List

class Actor(BaseModel):
    ac_id: int
    ac_name: str
    ac_email: str
    ac_dept: str
    #ac_customer:List[str]
    #pid:int
    #sid:int

db = [{'ac_id':'-','ac_name':'-','ac_email':'-','ac_dept':'-'}]

actor=APIRouter()

@actor.get('/', response_model=List[Actor])
async def index():
    return db

@actor.post('/', status_code=201)
async def add_a(payload: Actor):
    act= payload.dict()
    db.append(act)
    return {'id': len(db) - 1}

@actor.put('/{id}')
async def update_a(id: int, payload: Actor):
    a = payload.dict()
    a_length = len(db)
    if 0 <= id <= a_length:
        db[id] = a
        return None
    raise HTTPException(status_code=404, detail="actor with given id not found")

@movies.delete('/{id}')
async def delete_a(id: int):
    length = len(db)
    if 0 <= id <= length:
        del db[id]
        return None
    raise HTTPException(status_code=404, detail="actor with given id not found")