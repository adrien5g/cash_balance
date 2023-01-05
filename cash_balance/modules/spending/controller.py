from fastapi import APIRouter, Depends
from sqlmodel import Session
from .entities import (
    SpendingEntity, SpendingTagLinkEntity, SpendingTagsEntity
)

from libs.api.auth import get_current_user
from libs.database import get_session

from .models import AllSpendings
from .repositories import SpendingRepository


class SpendingController:

    router = APIRouter(prefix='/spending')

    @router.get('/get', response_model=AllSpendings)
    def get_spendings(
        user_uuid = Depends(get_current_user),
        spending_repository: SpendingRepository = Depends(SpendingRepository),
        session: Session = Depends(get_session)
    ):
        spendings = spending_repository.get_spendings(user_uuid['sub'], session)
        print(spendings)
        return spendings