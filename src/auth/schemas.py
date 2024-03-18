from uuid import uuid4

from pydantic import Field

from src.schemas import CustomBaseModel


class User(CustomBaseModel):
    oid: str = Field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    username: str
    email: str | None = None

    def __str__(self):
        return f'username={self.username} email={self.email}'

    def __hash__(self):
        return hash(self.oid)

    def __eq__(self, other: 'User'):
        return self.oid == other.oid
