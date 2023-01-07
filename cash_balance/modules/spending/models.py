from typing import List
from pydantic import BaseModel
from datetime import date

class Spending(BaseModel):
    name: str
    value: str
    uuid: str

class AllTagsModel(BaseModel):
    uuid: str

class AllSpendingsModel(BaseModel):
    name: str
    note: str
    value: str
    uuid: str
    tags: List[AllTagsModel]

class AllSpendings(BaseModel):
    spendings: List[AllSpendingsModel]

class NewSpending(BaseModel):
    name: str
    note: str
    value: str
    spending_date: date
    tags: List[str]

class NewTag(BaseModel):
    name: str
    description: str

class NewTagResponse(NewTag):
    uuid: str