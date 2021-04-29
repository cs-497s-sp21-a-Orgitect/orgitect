# Yidan Gong

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
* API information can be checked at http://localhost:8000/docs

# API:
https://app.swaggerhub.com/apis/gydddd/fast-api/0.1.0

# Database:
* The graph below shows the current structure of actor table. It will use http requests to retrieve information of each stage id in sid.


