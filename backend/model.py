from pydantic import BaseModel,Field
from uuid import UUID,uuid4


class BudgetItem(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name: str
    price: float
    tag: str = "untagged"