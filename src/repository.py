from abc import ABC, abstractmethod

from .models import BaseModel


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abstractmethod
    def get(self, model, ref):
        raise NotImplementedError


# TODO: make it asynchronous
class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, model: BaseModel) -> None:
        self.session.add(model)
        self.session.commit()

    def get(self, model: BaseModel, pk: int) -> BaseModel:
        obj = self.session.get(model, pk)
        return obj
