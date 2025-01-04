
from fastapi.testclient import TestClient
from app.main import app

#creating a test client for this app that requests to the server
client = TestClient(app)

#i wanna test the get response of homepage

def test_get_home():
    response = client.get("/") #requests.get("") python requests
    assert response.text != "<h1>Hello World</h1>"

    #this status_code=200 so test will pass if 200=200
    assert response.status_code ==200

    #test if text/html is in response.headers
    assert "text/html" in response.headers['content-type']

def test_post_home():
    response = client.post("/")
    assert response.status_code ==200
    assert "application/json" in response.headers['content-type']

    assert response.json() == {"hello": "world"}


