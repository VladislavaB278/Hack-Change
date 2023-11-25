from sqlalchemy import select, update

from src.models.rooms import UsersRooms
from src.models.users import Users
from src.utils.repository import SQLAlchemyRepository


class UsersRoomsRepository(SQLAlchemyRepository):
    model = UsersRooms

    async def find_users_room(self, room_id):
        stmt = (
            select(Users, self.model).join(Users, Users.id == self.model.user_id).where(self.model.room_id == room_id)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        print(res)
        res = [row.to_read_model() for row in res]
        return res

    async def edit_one(self, user_id: int, data: dict):
        stmt = update(self.model).values(**data).filter_by(user_id=user_id)
        await self.session.execute(stmt)
        await self.session.commit()
