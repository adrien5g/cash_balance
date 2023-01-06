from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from .models import RegisterUser, LoginUser
from .entities import UserEntity
from .ext import (
    UserNotFound, WrongPassword, UserAlreadyExists
)
from utils.crypt import crypt_password, verify_password

class UserRepository:

    @staticmethod
    def login_user(user: LoginUser, session: Session) -> UserEntity:
        query = select(UserEntity).where(UserEntity.username == user.username)
        login_user = session.exec(query).first()
        if not login_user:
            raise UserNotFound('User not found')
        elif not verify_password(login_user.password, user.password):
            raise WrongPassword('Wrong password')
        return login_user

    @staticmethod
    def create_user(user: RegisterUser, session: Session):
        query = select(UserEntity).where(UserEntity.username == user.username)
        existing_user = session.exec(query).first()
        if existing_user:
            raise UserAlreadyExists('User already exists')
        new_user = UserEntity.from_orm(user)
        new_user.password = crypt_password(new_user.password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    @staticmethod
    def get_user_by_uuid(user_uuid: str, session: Session):
        query = select(UserEntity).where(UserEntity.uuid == user_uuid).options(selectinload(UserEntity.spendings))
        user = session.exec(query).first()
        return user

    @staticmethod
    def all_users(session: Session):
        query = select(UserEntity).options(selectinload(UserEntity.spendings))
        all_users = session.exec(query).all()
        return all_users
