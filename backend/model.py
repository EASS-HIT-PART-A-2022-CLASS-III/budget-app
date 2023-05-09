from pydantic import BaseModel

class BudgetItem(BaseModel):
    name: str
    price: float
    tag: str = "untagged"