from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from modules.user.entities import UserEntity

class SpendingEntity(SQLModel, table=True):

    __tablename__ = 'spending'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str = Field(default=None, nullable=False)
    value: str = Field(default=None, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    spending_date: datetime = Field(nullable=False)
    user_id: str = Field(default=None, nullable=False, foreign_key='users.id')

    user: 'UserEntity' = Relationship(back_populates='spendings')
    tags: List['SpendingTagLinkEntity'] = Relationship(back_populates='spendings')

class SpendingTagsEntity(SQLModel, table=True):

    __tablename__ = 'spending_tags'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False)
    description: str = Field(default=None, nullable=False)
    spendings: List['SpendingEntity'] = Relationship(back_populates='tags')

    spendings: List['SpendingTagLinkEntity'] = Relationship(back_populates='tags')

class SpendingTagLinkEntity(SQLModel, table=True):

    __tablename__ = 'spending_tag_link'

    id: Optional[int] = Field(default=None, primary_key=True)
    tag_id: Optional[int] = Field(foreign_key='spending_tags.id')
    spending_id: Optional[int] = Field(foreign_key='spending.id')

    spendings: List[SpendingEntity] = Relationship(back_populates='tags')
    tags: List[SpendingTagsEntity] = Relationship(back_populates='spendings')
