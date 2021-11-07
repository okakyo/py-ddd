from py_server import __version__
from fastapi.testclient import TestClient
from py_server.main import app 

client = TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_hello_world():
    res = client.get("/")
    assert res.status_code==200
    assert res.json() =="Hello World"


