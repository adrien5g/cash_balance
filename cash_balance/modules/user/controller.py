from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from libs.database import get_session
from libs.api.auth import get_current_user, create_access_token, create_refresh_access_token

from .models import RegisterUser, ReadUser, LoginUser, AllData
from .ext import UserNotFound, WrongPassword, UserAlreadyExists
from .repositories import UserRepository

class UserController:
        
    router = APIRouter(prefix='/user')

    @router.get('/login', response_model=ReadUser)
    def user_login(
        user: LoginUser, 
        user_repository: UserRepository = Depends(UserRepository),
        session: Session = Depends(get_session)
    ):
        try:
            logged_user = user_repository.login_user(user, session)
        except UserNotFound:
            raise HTTPException(status_code=401, detail='User not found')
        except WrongPassword:
            raise HTTPException(status_code=401, detail='Wrong password')
        data = {
            'access_token': create_access_token(logged_user.uuid),
            'refresh_access_token': create_refresh_access_token(logged_user.uuid)
        }

        return {
            'status': 'success',
            'message': data
        }

    @router.post('/register', response_model=ReadUser)
    def user_register(
        user: RegisterUser, 
        user_repository: UserRepository = Depends(UserRepository),
        session: Session = Depends(get_session)
    ):
        try:
            new_user = user_repository.create_user(user, session)
        except UserAlreadyExists:
            raise HTTPException(status_code=409, detail='User already exists')
        data = {
            'access_token': create_access_token(new_user.uuid),
            'refresh_access_token': create_refresh_access_token(new_user.uuid)
        }

        return {
            'status': 'success',
            'message': data
        }

    @router.get('/all_users', response_model=List[AllData])
    def all_users(
        user_repository: UserRepository = Depends(UserRepository),
        session: Session = Depends(get_session)
    ):
        all_users = user_repository.all_users(session)
        return all_users

    @router.get('/me', response_model=AllData)
    def get_me(
        user = Depends(get_current_user), 
        user_repository: UserRepository = Depends(UserRepository),
        session: Session = Depends(get_session)
    ):
        user = user_repository.get_user_by_uuid(user['sub'], session)
        return user