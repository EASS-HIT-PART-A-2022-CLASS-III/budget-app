from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

budget = []


class BudgetItem(BaseModel):
    name: str
    price: float
    tag: Union[str, None] = None


@app.get("/")
async def landing_page():
    return {"message": "welcome to the site"}


@app.get("/budget_item/")
async def get_all_budget_items():
    return budget


@app.get("/budget_item/id")
async def get_budget_item_ids():
    result = {}
    for i in range(len(budget)):
        id = i
        name = budget[i].name
        result[id]=name
    if len(result) != 0:
        return result
    else:
        return {"message": "Budget is empty"}


@app.get("/budget_item/id/{item_id}")
async def get_budget_item_by_id(item_id: int):
    try:
        return budget[item_id]
    except IndexError:
        return {"message": "Budget item not found"}


@app.get("/budget_item/tag")
async def get_budget_item_tags():
    result = {}
    for item in budget:
        if item.tag not in result:
            result[item.tag]=1
        else:
            updated = result.get(item.tag)
            updated = updated+1
            result[item.tag] = updated
    if len(result) != 0:
        return result
    else:
        return {"message": "Budget has no tags"}


@app.get("/budget_item/{item_tag}")
async def get_budget_item_by_tag(item_tag: str):
    result = list(filter(lambda x: x.tag == item_tag, budget))
    if len(result) != 0:
        return result
    else:
        return {"message": "Budget item not found"}


@app.post("/budget_item/", response_model=BudgetItem)
async def add_budget_item(item: BudgetItem):
    budget.append(item)
    return item


@app.put("/budget_item/{item_id}")
async def edit_budget_item(item_id: int, Name: str, Price: float, Tag: str):
    try:
        budget[item_id].name = Name
        budget[item_id].price = Price
        budget[item_id].tag = Tag
        return {"message": "Budget item updated succcessfully"}
    except IndexError:
        return {"message": "Budget item not found"}
