from fastapi.testclient import TestClient
from .main import app
import pytest

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to the site"}

def test_post_item():
    response = client.post("/budget_item/", json={"name": "pizza", "price": 100, "tag":"food"})
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "food"}

def test_read_budget():
    response = client.get("/budget_item/")
    assert response.status_code == 200
    assert response.json() == {"food": 100}

def test_remove_item():
    response = client.delete("/budget_item/0")
    assert response.status_code == 200
    assert response.json() == {"message": "Budget item removed succcessfully"}


def test_post_item_no_tag():
    response = client.post("/budget_item", json={"name":"pizza","price":100})
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "untagged"}

def test_read_all_ids():
    response = client.get("/budget_item/id")
    assert response.status_code == 200
    assert response.json() == {"0":"pizza"}