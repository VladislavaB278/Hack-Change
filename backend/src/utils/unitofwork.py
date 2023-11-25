from abc import ABC, abstractmethod

from src.database.database import async_session
from src.repositories.users import UsersRepository
from src.repositories.rooms import RoomsRepository
from src.repositories.users_rooms import UsersRoomsRepository


class IUnitOfWork(ABC):
    users: UsersRepository
    rooms: RoomsRepository
    users_rooms: UsersRoomsRepository

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UsersRepository(self.session)
        self.rooms = RoomsRepository(self.session)
        self.users_rooms = UsersRoomsRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
