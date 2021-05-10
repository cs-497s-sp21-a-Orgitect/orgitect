from fastapi import Header, APIRouter,HTTPException, Request
from fastapi.templating import Jinja2Templates
from app.api import request as req
import json

actorre=APIRouter()

#GET unsigned requests 
@actorre.get("/")
async def get_unassigned_req(request: Request):
    templates = Jinja2Templates(directory="templates")
    a=req.get_unassigned_request()
    d = json.loads(a)
    return templates.TemplateResponse("ureq.html", 
    {"request": request,'title':"Unassigned Requests",'users':d['results'],'button':'select'})


