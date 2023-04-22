from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_full():
    response = client.get("/")
    response = client.post(
        "/budget_item/", json={"name": "pizza", "price": 100, "tag": "food"}
    )
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "food"}

    response = client.get("/budget_item/")
    assert response.status_code == 200
    assert response.json() == {"food": 100}

    response = client.delete("/budget_item/0")
    assert response.status_code == 200
    assert response.json() == {"message": "Budget item removed succcessfully"}

    response = client.post("/budget_item", json={"name": "pizza", "price": 100})
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "untagged"}

    response = client.get("/budget_item/id")
    assert response.status_code == 200
    assert response.json() == {"0": "pizza"}

    response = client.put(
        "/budget_item/0", json={"name": "pizza", "price": 100, "tag": "food"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Budget item updated succcessfully"}

    response = client.get("/budget_item/tag/food")
    assert response.status_code == 200
    assert response.json() == {"pizza": 100}

    response = client.get("/budget_item/id/0")
    assert response.status_code == 200
    assert response.json() == {"name": "pizza", "price": 100, "tag": "food"}

    client.close()

  

