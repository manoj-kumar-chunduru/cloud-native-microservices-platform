from fastapi.testclient import TestClient
from app.main import app,USERS
client=TestClient(app)
def setup_function(): USERS.clear()
def test_health(): assert client.get('/health').json()=={'status':'UP'}
def test_create_and_read():
    x=client.post('/api/v1/users',json={'name':'Manoj','email':'m@example.com'}); assert x.status_code==201
    uid=x.json()['id']; y=client.get(f'/api/v1/users/{uid}'); assert y.status_code==200 and y.json()['email']=='m@example.com'
def test_validation(): assert client.post('/api/v1/users',json={'name':'M','email':'bad'}).status_code==422
def test_missing(): assert client.get('/api/v1/users/99999').status_code==404
