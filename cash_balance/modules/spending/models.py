from typing import List
from pydantic import BaseModel

class Spending(BaseModel):
    name: str
    value: str
    tags: List[int]

class AllSpendings(BaseModel):
    List[Spending]