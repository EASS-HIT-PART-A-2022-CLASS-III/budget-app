from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to the site"}


def test_read_budget():
    response = client.get("/budget_item/")
    assert response.status_code == 200
    assert response.json() == []


def test_post_item():
    response = client.post("/budget_item/", json={"name": "pizza", "price": 100, "tag":"food"})
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "food"}

def test_post_item_no_tag():
    response = client.post("/budget_item", json={"name":"pizza","price":100,})
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": None}

def test_read_all_ids():
    client.post("/budget_item/", json={"name": "pizza", "price": 100, "tag":"food"})
    response = client.get("/budget_item/id")
    assert response.status_code == 200
    assert response.json() == {"id":0,"name":"pizza"}