from fastapi import APIRouter, Depends
from starlette import status

from src.models.users import Users
from src.models.rooms import RoomsSchema
from src.schemas.room import UsersRoomsAdd, UsersIdScheme
from src.schemas.users import UsersRead
from src.security import get_current_user
from src.services import room_service
from src.utils.dependencies import UOWDep

router = APIRouter(prefix="/api/rooms", tags=["Rooms"], responses={404: {"description": "Not found"}})


@router.get("/{room_id}", response_model=RoomsSchema)
async def get_room(room_id: int, uow: UOWDep, _: Users = Depends(get_current_user)):
    rooms = await room_service.get_room(room_id, uow)
    return rooms


@router.post("/", response_model=RoomsSchema)
async def add_room(uow: UOWDep, user: Users = Depends(get_current_user)):
    room = await room_service.add_room(uow, user)
    return room


@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(uow: UOWDep, room_id: int, user: Users = Depends(get_current_user)):
    await room_service.delete_room(uow, room_id, user)


@router.post("/add_user")
async def add_user_room(uow: UOWDep, data: UsersRoomsAdd, user: Users = Depends(get_current_user)):
    await room_service.add_user_room(uow, data, user)
    return {"status": "successful"}


@router.delete("/remove_user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user_room(uow: UOWDep, user_id: int, user: Users = Depends(get_current_user)):
    await room_service.remove_users_room(uow, user_id, user)


@router.get("/{room_id}/users", response_model=list[UsersRead])
async def get_users_room(uow: UOWDep, room_id: int, _: Users = Depends(get_current_user)):
    users = await room_service.get_users_room(uow, room_id)
    return users


@router.patch("/set_leaders")
async def set_leader(uow: UOWDep, data: UsersIdScheme, user: Users = Depends(get_current_user)):
    await room_service.set_leaders(uow, data, user)
    return {"status": "successful"}
