from src.schemas import CustomBaseModel


class User(CustomBaseModel):
    username: str
    email: str | None = None

    def __str__(self):
        return f'username={self.username} email={self.email}'
