from typing import Optional, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]]
    notes: Mapped[List['Note']] = relationship(back_populates='user')

    def __repr__(self):
        return f'User(user_id={self.user_id} email={self.email})'
