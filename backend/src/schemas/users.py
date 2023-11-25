from datetime import datetime

from pydantic import BaseModel, EmailStr


class UsersRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_at: datetime
    is_admin: bool


class UsersSchema(UsersRead):
    password: str


class UsersCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int


class UsersAdmin(BaseModel):
    id: int | None = None
    username: str | None = None
    email: EmailStr | None = None
    registered_at: datetime | None = None
    is_admin: bool | None = None
    password: int | None = None
