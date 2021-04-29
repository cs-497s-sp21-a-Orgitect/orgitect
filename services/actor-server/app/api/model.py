from pydantic import BaseModel
from typing import List, Optional

class ActorIn(BaseModel):
    ac_name: str
    ac_email: str 
    ac_dept: str 
    ac_customer:List[str] = None
    sid:List[int] = None

class ActorOut(ActorIn):
    id: int

class ActorUpdate(ActorIn):
    ac_name: Optional[str] = None
    ac_email: Optional[str] = None
    ac_dept: Optional[str]= None
    ac_customer: Optional[List[str]] = None
    sid: Optional[List[int]] = None
