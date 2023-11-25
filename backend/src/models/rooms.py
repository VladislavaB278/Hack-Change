from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base
from src.schemas.room import RoomsSchema, UsersRoomsSchema


class Rooms(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    def to_read_model(self) -> RoomsSchema:
        return RoomsSchema(id=self.id)


class UsersRooms(Base):
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False
    )
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    is_leader: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def to_read_model(self) -> UsersRoomsSchema:
        return UsersRoomsSchema(user_id=self.user_id, room_id=self.room_id, is_leader=self.is_leader)
