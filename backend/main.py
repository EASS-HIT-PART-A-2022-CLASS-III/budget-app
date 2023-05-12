from fastapi import FastAPI
from model import BudgetItem
from uuid import UUID

app = FastAPI()

budget = []

budgetV2 = {}


@app.get("/")
async def landing_page():
    return {"message": "welcome to the site"}


@app.get("/v1/budget_item/")
async def get_all_budget_items_v1():
    result = {}
    for item in budget:
        if item.tag not in result:
            result[item.tag] = item.price
        else:
            result[item.tag] = result[item.tag] + item.price
    if len(result) != 0:
        return result
    else:
        return {"error": "budget is empty"}
    

@app.get("/v2/budget_item/")
async def get_all_budget_items_v2():
    result = {}
    for value in budgetV2.values():
        if value["tag"] not in result:
            result[value["tag"]] = value["price"]
        else:
            result[value["tag"]] = result[value["tag"]] + value["price"]
    if len(result) != 0:
        return result
    else:
        return {"error": "budget is empty"}


@app.get("/v1/budget_item/id")
async def get_budget_item_ids_v1():
    result = {}
    for i in range(len(budget)):
        id = i
        name = budget[i].name
        result[id] = name
    if len(result) != 0:
        return result
    else:
        return {"error": "Budget is empty"}

@app.get("/v2/budget_item/id")
async def get_budget_item_ids_v2():
    result={}
    keys = budgetV2.keys()
    i = 0
    for key in keys:
        result[i] = key
        i+=1
    if len(result)!= 0:
        return result
    else:
        return {"error": "Budget is empty"}

@app.get("/v1/budget_item/id/{item_id}")
async def get_budget_item_by_id_v1(item_id: int):
    try:
        return budget[item_id]
    except IndexError:
        return {"error": "Budget item not found"}

@app.get("/v2/budget_item/id/{item_id}")
async def get_budget_item_by_id_v2(item_id:UUID):
    try:
        return budgetV2[item_id]
    except KeyError:
        return {"error": "Budget item not found"}

@app.get("/v1/budget_item/tag")
async def get_budget_item_tags_v1():
    result = {}
    for item in budget:
        if item.tag not in result:
            result[item.tag] = 1
        else:
            result[item.tag] = result.get(item.tag) + 1
    if len(result) != 0:
        return result
    else:
        return {"error": "Budget has no tags"}

@app.get("/v2/budget_item/tag")
async def get_budget_item_tags_v2():
    result = {}
    for item in budgetV2.values():
        if item["tag"] not in result:
            result[item["tag"]] = 1
        else:
            result[item["tag"]] = result.get(item["tag"]) + 1
    if len(result) != 0:
        return result
    else:
        return {"error": "Budget has no tags"}

@app.get("/v1/budget_item/tag/{item_tag}")
async def get_budget_item_by_tag_v1(item_tag: str):
    result = {}
    for item in budget:
        if item.tag == item_tag:
            if item.name not in result:
                result[item.name] = item.price
            else:
                result[item.name] = result[item.name] + item.price
    if len(result) != 0:
        return result
    else:
        return {"error": "tag not found in budget"}
    

@app.get("/v2/budget_item/tag/{item_tag}")
async def get_budget_item_by_tag_v2(item_tag: str):
    result = {}
    for item in budgetV2.values():
        if item["tag"] == item_tag:
            if item["name"] not in result:
                result[item["name"]] = item["price"]
            else:
                result[item["name"]] = result[item["name"]] + item["price"]
    if len(result) != 0:
        return result
    else:
        return {"error": "tag not found in budget"}


@app.post("/v1/budget_item/", response_model=BudgetItem)
async def add_budget_item_v1(item: BudgetItem):
    budget.append(item)
    return item

@app.post("/v2/budget_item/")
async def add_budget_item_v2(Name: str,Price: float,Tag: str = "untagged"):
    item = BudgetItem(name=Name,price=Price,tag=Tag)
    budgetV2[item.id] = {"name":item.name,"price":item.price,"tag":item.tag}
    return item

@app.put("/v1/budget_item/{item_id}")
async def edit_budget_item_v1(item: BudgetItem, item_id: int):
    try:
        budget[item_id].name = item.name
        budget[item_id].price = item.price
        budget[item_id].tag = item.tag
        return {"message": "Budget item updated succcessfully"}
    except IndexError:
        return {"error": "Budget item not found"}
    
@app.put("/v2/budget_item/{item_id}")
async def edit_budget_item_v2(Name: str,Price: float,Tag: str, item_id: UUID):
    try:
        budgetV2[item_id]["name"] = Name
        budgetV2[item_id]["price"] = Price
        budgetV2[item_id]["tag"] = Tag
        return {"message": "Budget item updated succcessfully"}
    except KeyError:
        return {"error": "Budget item not found"}


@app.delete("/v1/budget_item/{item_id}")
async def remove_budget_item_v1(item_id: int):
    try:
        budget.pop(item_id)
        return {"message": "Budget item removed succcessfully"}
    except IndexError:
        return {"error": "Budget item not found"}

@app.delete("/v2/budget_item/{item_id}")
async def remove_budget_item_v2(item_id: UUID):
    try:
        budgetV2.pop(item_id)
        return {"message": "Budget item removed succcessfully"}
    except KeyError:
        return {"error": "Budget item not found"}