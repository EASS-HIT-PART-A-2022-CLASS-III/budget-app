from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to the site"}


def test_post_item():
    response = client.post(
        "http://localhost:8000/v3/budget_item?Name=piza&Price=80&Tag=food"
    )
    assert response.status_code == 200


def test_read_budget():
    response = client.get("/v3/budget_item/")
    assert response.status_code == 200


def test_read_all_ids():
    response = client.get("v3/budget_item/id")
    assert response.status_code == 200


def test_spesific_id():
    first_response = client.get("v3/budget_item/id").json
    item_id = first_response[len(first_response) - 1]
    response = client.get(f"v3/budget_item/id/{item_id}")
    assert response.status_code == 200


def test_spesific_tag():
    response = client.get("v3/budget_item/tag")
    assert response.status_code == 200


def test_item_edit():
    first_response = client.get("v3/budget_item/id").json
    item_id = first_response[len(first_response) - 1]
    response = client.put(f"/v3/budget_item/{item_id}?Name=pizza&Price=80&Tag=food")
    assert response.status_code == 200


def test_remove_item():
    first_response = client.get("v3/budget_item/id").json
    item_id = first_response[len(first_response) - 1]
    response = client.delete(f"v3/budget_item/{item_id}")
    assert response.status_code == 200


def test_spesific_tag():
    response = client.get("http://localhost:8000/v3/budget_item/tag/food")
    assert response.status_code == 200
