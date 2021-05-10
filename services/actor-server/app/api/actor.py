from fastapi import Header, APIRouter,HTTPException, Request
from pydantic import BaseModel
from typing import List,Optional
from app.api.model import ActorIn, ActorOut, ActorUpdate
from app.api import db_manager
from app.api import request as req
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json

actor=APIRouter()

templates = Jinja2Templates(directory="templates")

#get all actor
@actor.get('/', response_model=List[ActorOut])
async def index():
    return await db_manager.get_all_actor()

#GET information of an actor using actor from client request
#return html of actor profile
@actor.get("/{id}", response_class=HTMLResponse)
async def get_actor(request: Request, id: int):
    a=await db_manager.get_actor(id)
    return templates.TemplateResponse("index.html", 
    {"request": request, "id": a['id'],"name":a['ac_name'],'users':a['ac_customer']})

#GET request for a customer and a actor
@actor.get("/{id}/{cid}")
async def get_customer(request:Request,id:int,cid:int):
    a=req.get_stage_request(id,cid).decode()
    d = json.loads(a)
    #remove the customer if no request
    if d['count'] is 0:
        res = await db_manager.get_actor(id)
        si =res['ac_customer']
        si.remove(cid)
        update_data={'ac_customer':si}
        a_in_db = ActorIn(**res)
        updated_a= a_in_db.copy(update=update_data)
        return await db_manager.update_actor(id, updated_a)
    return templates.TemplateResponse("req.html", 
    {"request": request,"title":"Customer requests","users":d['results'],"button":"update",
    "currs":"current stage information"})

#POST create actor
@actor.post('/', status_code=201)
async def add_a(payload: ActorIn):
    actor_id = await db_manager.add_actor(payload)
    response = {
        'id': actor_id,
        **payload.dict()
    }
    print(response)
    #request.req_org(response['ac_dept'],response['id'])
    return 

#changing customer stage
@actor.get("/{id}/{cid}/{sid}")
async def update_stage(request:Request,id:int,cid:int,sid:int):
    #send put request to stage
    res=req.update_stage(sid).decode()
    d=json.loads(res)
    print(d)
    curr=d["result"]["currentStage"]
    if not curr:
        #send post req to notification
        #complete_stage(cid)
        a = await db_manager.get_actor(id)
        si =a['sid']
        si.remove(sid)
        update_data={'sid':si}
        a_in_db = ActorIn(**a)
        updated_a= a_in_db.copy(update=update_data)
        return await db_manager.update_actor(id, updated_a)
    return
    
#PUT update fields of an actor
#selecting a customer:{'ac_customer':[1],'sid':[2]}
@actor.put('/{id}')
async def update_a(id: int, payload: ActorUpdate):
    a = await db_manager.get_actor(id)
    if not a:
        raise HTTPException(status_code=404, detail="actor with given id not found")
    update_data = payload.dict(exclude_unset=True)
    if update_data['ac_customer'] and update_data['sid']:
        sid=update_data['sid'][0]
        re=req.update_stage_a(sid,id)
    a_in_db = ActorIn(**a)
    updated_a= a_in_db.copy(update=update_data)
    return await db_manager.update_actor(id, updated_a)

#DELETE actor
@actor.delete('/{id}')
async def delete_a(id: int):
    actor=await db_manager.delete_actor(id)
    if not actor:
        raise HTTPException(status_code=404,detail="no such actor")
    return await db_manager.delete_actor(id)

