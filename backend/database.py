import motor.motor_asyncio
from bson.binary import UuidRepresentation

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:secret@db:27017',UuidRepresentation='standard')

db = client.budget_database

colletion = db.budget_table

async def get_all_budget_items():
    result = {}
    items = colletion.find({})
    async for item in items:
        result[item["id"]] =  {"name":item['name'],'price':item['price'],'tag':item['tag']}
    return result

async def get_budget_item_ids():
    result={}
    items = colletion.find({})
    i = 0
    for item in items:
        result[i] = item["id"]
        i+=1
    if len(result)!= 0:
        return result
    else:
        return {"error": "Budget is empty"} 

async def insert_budget_item(item):
    await colletion.insert_one(item)
    return item