import pprint
from typing import List
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from .entities import SpendingEntity, SpendingTagLinkEntity, SpendingTagsEntity
from .models import NewSpending, NewTag

class SpendingRepository:

    @staticmethod
    def get_spendings(user_uuid: str, session: Session) -> List[SpendingEntity]:
        query = select(SpendingEntity)\
            .options(selectinload(SpendingEntity.tags))\
            .where(SpendingEntity.user_id == user_uuid)

        spendings = session.exec(query).all()
        return spendings

    @staticmethod
    def new_spending(spending: NewSpending, user_uuid: str, session: Session):
        new_spending = SpendingEntity.from_orm(spending)
        new_spending.user_id = user_uuid
        session.add(new_spending)
        for tag in spending.tags:
            tag_link = SpendingTagLinkEntity(tag_id=tag, spending_id=new_spending.uuid)
            session.add(tag_link)
        session.commit()
        session.refresh(new_spending)
        return new_spending

    @staticmethod
    def new_spending_tag(tag: NewTag, user_uuid: str,  session: Session):
        new_tag = SpendingTagsEntity.from_orm(tag)
        new_tag.user_id = user_uuid
        session.add(new_tag)
        session.commit()
        session.refresh(new_tag)
        return new_tag