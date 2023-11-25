from pydantic import BaseModel


class RoomsSchema(BaseModel):
    id: int


class UsersRoomsSchema(BaseModel):
    room_id: int
    user_id: int
    is_leader: bool


class UsersRoomsCreate(BaseModel):
    room_id: int
    user_id: int


class UsersIdScheme(BaseModel):
    user_id: int


class UsersRoomsAdd(BaseModel):
    room_id: int


class UsersRoomsUpdate(BaseModel):
    user_id: int
    is_leader: bool
