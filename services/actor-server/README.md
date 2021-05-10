# Yidan Gong
```
  docker build -t myimage .
  docker run -d --name mycontainer -p 80:80 myimage
```

# Developing environment:
```
pip install virtualenv or pip install venv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
* Run server:
```
./start
uvicorn main:app/
```
* exit environment
```
deactivate
```
* API information can be checked at 

# API:
https://app.swaggerhub.com/apis-docs/gydddd/fast-api/0.1.2

# Database:
* The graph below shows the current structure of actor table. It will use http requests to retrieve information of each stage id in sid.


