import datetime

from sqlalchemy import mapped_column, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.models import BaseModel
from src.schemas import Status


class NoteModel(BaseModel):
    __tablename__ = 'notes'

    note_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    status: Mapped[Status]
    created_at: Mapped[datetime.datetime]
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    author: Mapped['User'] = relationship(
        back_populates='notes',
    )

    def __repr__(self):
        return (
            f'Note(note_id={self.note_id} '
            f'title={self.title} '
            f'description={self.description} '
            f'status={self.status.value} '
            f'created_at={self.create_at})'
        )
