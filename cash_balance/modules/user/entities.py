import uuid

from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from modules.spending.entities import SpendingEntity

class UserEntity(SQLModel, table=True):

    __tablename__ = 'users'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(default=str(uuid.uuid4()), index=True)
    full_name: str = Field(default=None, nullable=False)
    username: str = Field(default=None, nullable=False, index=True)
    password: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)

    spendings: List['SpendingEntity'] = Relationship(back_populates='user')
