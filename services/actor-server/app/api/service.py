import os
import requests
 
#send GET request to stage
#return data if 200
async def req_stage(sid:int):
     s=requests.get('http://localhost:8080/api/v1/stages/{sid}')
     c=s.content
     return c if s.status_code == 200 else False

#send POST request to organization
#return 402 or 200
async def req_org(orgid:int,aid:int):
     s=requests.post(data={'organizationId':orgid,"actorId":aid})
     return s

#send PUT request to stage
async def update_stage(sid:int):
     s=requests.put('http://localhost:8080/api/v1/stages/{sid}')
     return s

#send post to notification
async def complete_stage(email:str,name:str):
    s=request.post(data={'email':email,'name':name})
    return s