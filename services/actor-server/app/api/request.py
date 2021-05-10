import requests
import os

#example resp:'{"result":
# {"id":1,
# "process":{"id":1,"name":"Cancel Meal Plan","description":"Use this process to cancel a meal plan for a student",
# "stages":[{"id":1,"action":"Sign that the request has been completed","duration":20,"ordering":2},{"id":2,"action":"Refund funds to student account","duration":30,"ordering":1},{"id":3,"action":"Login to system and cancel student plan","duration":20,"ordering":0}]},
# "customerId":1,"actorId":1,
# "currentStage":{"id":1,"action":"Sign that the request has been completed","duration":20,"ordering":2}}}'


#GET request to stage to get unassigned requests
def get_unassigned_request():
    s=requests.get('http://localhost:8080/api/v1/request/unassigned')
    c= s.content
    return c if s.status_code == 200 else False
    

#GET request for actor and customer 
#return data if 200
def get_stage_request(i:int,cid:int):
   url="http://localhost:8080/api/v1/request/customer/{cid}/actor/{id}".format(cid=cid,id=i)
   s=requests.get(url) 
   c=s.content
   return c if s.status_code == 200 else False
   

#send POST request to organization
#return 402 or 200
async def req_org(orgid:int,aid:int):
     s=requests.post('/organizations/members', data={'organizationId':orgid,"actorId":aid})
     print(s)

#send PUT request to stage
def update_stage(sid:int):
     s=requests.post('http://localhost:8080/api/v1/request/%s/nextStage'%sid,data={})
     c=s.content
     return c if s.status_code == 200 else False

#update actor request
def update_stage_a(sid:int,i:int):
     s=requests.put('http://localhost:8080/api/v1/request/%s/actor/%s'%(sid,i),data={})
     c=s.content
     return c if s.status_code == 200 else False

'''
#send POST request to organization
#return 402 or 200
async def req_org(orgid:int,aid:int):
     s=requests.post(data={'organizationId':orgid,"actorId":aid})
     return s

#send post to notification with customer id
async def complete_stage(email:str,name:str):
    s=request.post(data={'c_id':customer_id})
    return s
'''


