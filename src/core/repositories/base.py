from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self):
        ...

    @abstractmethod
    async def get_all(self):
        ...
