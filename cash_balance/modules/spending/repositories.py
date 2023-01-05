from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from .entities import SpendingEntity, SpendingTagLinkEntity

class SpendingRepository:

    @staticmethod
    def get_spendings(user_uuid: str, session: Session):
        query = select(SpendingEntity)\
            .options(selectinload(SpendingEntity.tags))\
            .where(SpendingEntity.user_id == user_uuid)
        # query = select(SpendingEntity)\
        #     .options(selectinload(SpendingTagLinkEntity.tag_id))\
        #     .where(SpendingEntity.user_id == user_uuid)
        spendings = session.exec(query).all()
        return spendings