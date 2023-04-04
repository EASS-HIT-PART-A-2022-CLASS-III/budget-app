from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
app = FastAPI()

budget=[]

class BudgetItem(BaseModel):
    name: str
    price: float
    tag: Union[str,None] = None

@app.get("/budget_item/")
async def get_all_budget_items():
    return budget


@app.get("/budget_item/{item_parameter}")
async def get_budget_item_by_parameter(item_parameter: int):
    try:
        return budget[item_parameter]
    except IndexError:
        return {"message": "Budget item not found"}

@app.get("/budget_item/{item_parameter}")
async def get_budget_item_by_parameter(item_parameter:str):
    result = list(filter(lambda x: x.tag==item_parameter,budget))
    if len(result)!=0:
        return result
    else:
        return {"message": "Budget item not found"}


@app.post("/budget_item/")
async def add_budget_item(Name: str,Price: float,Tag: str = None):
    item = BudgetItem(name=Name,price=Price,tag=Tag)
    budget.append(item)
    return budget

@app.put("/budget_item/{item_id}")
async def edit_budget_item(item_id:int,Name:str,Price:float,Tag:str):
    try:
        budget[item_id].name=Name
        budget[item_id].price=Price
        budget[item_id].tag=Tag
        return {"message":"Budget item updated succcessfully"}
    except IndexError:
        return {"message":"Budget item not found"}
