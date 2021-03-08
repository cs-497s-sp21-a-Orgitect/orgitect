import requests, json

url='https:'
#making a post request 
requests.post(url, data={'key':'value'})
#making a get request that accept json
request.get(url,params={},headers={'Accept': 'application/json'})
#making a put request
requests.put('https://httpbin.org/put', data={'key':'value'})
#making a delete request
requests.delete('https://httpbin.org/delete')
#parse a valid JSON from the get request and convert it into a Python Dictionary
res1= json.loads(requests.get(url).text)
#parse python dictionary to json 
j=json.dumps(res1)
