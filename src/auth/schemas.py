from src.schemas import CustomBaseModel, BaseOutModel


class BaseUserModel(CustomBaseModel):
    pass


class UserCreate(BaseUserModel):
    username: str
    email: str | None = None

    def __str__(self):
        return f'UserCreateScheme(username={self.username} email={self.email})'


class UserOut(BaseOutModel, BaseUserModel):
    username: str
    email: str | None = None

    def __str__(self):
        return f'UserOutScheme(id={self.id} username={self.username} email={self.email})'


class UserUpdate(UserCreate):
    pass
