# Build environment:
```
pip install venv
source actor-server/env/bin/activate
pip install -r requirements.txt
```
* exit environment
```
deactivate
```

# Run server:
```
./start
uvicorn main:app
```
* API information can be checked at http://localhost:8000/docs

