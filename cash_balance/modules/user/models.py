from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class RegisterUser(UserBase):
    full_name: str
    password: str
    email: str

class LoginUser(UserBase):
    username: str
    password: str

class AccessToken(BaseModel):
    access_token: str
    refresh_access_token: str

class ReadUser(BaseModel):
    status: str
    message: AccessToken

class AllData(UserBase):
    id: int
    full_name: str
    password: str
    email: str
    spendings: list
