import pprint
from fastapi import APIRouter, Depends
from sqlmodel import Session
from .entities import (
    SpendingEntity, SpendingTagLinkEntity, SpendingTagsEntity
)

from libs.api.auth import get_current_user
from libs.database import get_session

from .models import Spending, AllSpendings, NewSpending, NewTag, NewTagResponse
from .repositories import SpendingRepository


class SpendingController:

    router = APIRouter(prefix='/spending')

    @router.get('/get', response_model=AllSpendings)
    def get_spendings(
        user_uuid = Depends(get_current_user),
        spending_repository: SpendingRepository = Depends(SpendingRepository),
        session: Session = Depends(get_session)
    ):
        spendings = spending_repository.get_spendings(user_uuid, session)
        list_of_spends = []
        for current_spending in spendings:
            tags = [{'uuid': tag.tag_id} for tag in current_spending.tags]
            spending = current_spending.dict()
            spending['tags'] = tags
            list_of_spends.append(spending)
        return {
            'spendings': list_of_spends
        }


    @router.post('/new', response_model=Spending)
    def new_spending(
        spending: NewSpending,
        user_uuid = Depends(get_current_user),
        spending_repository: SpendingRepository = Depends(SpendingRepository),
        session: Session = Depends(get_session)
    ):
        new_spending = spending_repository.new_spending(spending, user_uuid, session)
        return new_spending.dict()

    @router.post('/tag/new', response_model=NewTagResponse)
    def new_tag(
        tag: NewTag,
        user_uuid = Depends(get_current_user),
        spending_repository: SpendingRepository = Depends(SpendingRepository),
        session: Session = Depends(get_session)
    ):
        new_tag = spending_repository.new_spending_tag(tag, user_uuid, session)
        return new_tag.dict()