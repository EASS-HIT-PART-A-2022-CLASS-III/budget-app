import motor.motor_asyncio
from bson.binary import UuidRepresentation

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://root:secret@db:27017", UuidRepresentation="standard"
)

db = client.budget_database

colletion = db.budget_table


async def get_all_budget_items():
    result = {}
    items = colletion.find()
    async for item in items:
        result[item["id"]] = {
            "name": item["name"],
            "price": item["price"],
            "tag": item["tag"],
        }
    if len(result) != 0:
        return result
    else:
        return {"error": "budget is empty"}


async def get_budget_item_ids():
    result = {}
    items = colletion.find()
    i = 0
    async for item in items:
        result[i] = item["id"]
        i += 1
    if len(result) != 0:
        return result
    else:
        return {"error": "Budget is empty"}


async def get_budget_item_by_id(item_id):
    result = {}
    response = await colletion.find_one({"id": item_id})
    result[response["id"]] = {
        "name": response["name"],
        "price": response["price"],
        "tag": response["tag"],
    }
    if result:
        return result
    else:
        return {"error": "Budget item not found"}


async def get_budget_item_tags():
    result = {}
    items = colletion.find()
    async for item in items:
        if item["tag"] not in result:
            result[item["tag"]] = 1
        else:
            result[item["tag"]] = result.get(item["tag"]) + 1
    if len(result) != 0:
        return result
    else:
        return {"error": "Budget has no tags"}


async def get_budget_item_by_tag(item_tag):
    result = {}
    items = colletion.find({"tag": item_tag})
    async for item in items:
        result[item["id"]] = {
            "name": item["name"],
            "price": item["price"],
            "tag": item["tag"],
        }
    if len(result) != 0:
        return result
    else:
        return {"error": "budget is empty"}


async def add_budget_item(item):
    result = await colletion.insert_one(item)
    if result:
        return item
    else:
        return {"error": "Budget item could not be added"}


async def edit_budget_item(Name: str, Price: float, Tag: str, item_id):
    result = await colletion.update_one(
        {"id": item_id}, {"$set": {"name": Name, "price": Price, "tag": Tag}}
    )
    if result:
        return {"message": "Budget item updated succcessfully"}
    else:
        return {"error": "Budget item not found"}


async def remove_budget_item(item_id):
    check = await colletion.find({"id": item_id}).to_list(None)
    if check:
        result = await colletion.delete_one({"id": item_id})
        if result:
            return {"message": "Budget item removed succcessfully"}
    else:
        return {"error": "Budget item not found"}
