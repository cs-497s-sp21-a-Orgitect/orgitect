from fastapi import Header, APIRouter,HTTPException, Request
from pydantic import BaseModel
from typing import List,Optional
from app.api.model import ActorIn, ActorOut, ActorUpdate
from app.api import db_manager
from app.api import service
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

actor=APIRouter()

templates = Jinja2Templates(directory="templates")

#get all actor
@actor.get('/', response_model=List[ActorOut])
async def index():
    return await db_manager.get_all_actor()

#get one actor
#return html of actor profile
@actor.get("/{id}", response_class=HTMLResponse)
async def get_actor(request: Request, id: int):
    a=await db_manager.get_actor(id)
    return templates.TemplateResponse("index.html", 
    {"request": request, "id": a['id'],"name":a['ac_name']})

#create actor
@actor.post('/', status_code=201)
async def add_a(payload: ActorIn):
    actor_id = await db_manager.add_actor(payload)
    response = {
        'id': actor_id,
        **payload.dict()
    }
    return response

#update actor
@actor.put('/{id}')
async def update_a(id: int, payload: ActorUpdate):
    a = await db_manager.update_actor(id,payload)
    if not a:
        raise HTTPException(status_code=404, detail="actor with given id not found")
    update_data = payload.dict(exclude_unset=True)
    a_in_db = ActorIn(**a)
    updated_a= a_in_db.copy(update=update_data)
    return await db_manager.update_actor(id, updated_a)

#delete an actor
@actor.delete('/{id}')
async def delete_a(id: int):
    actor=await db_manager.delete_actor(id)
    if not actor:
        raise HTTPException(status_code=404,detail="no such actor")
    return await db_manager.delete_actor(id)

