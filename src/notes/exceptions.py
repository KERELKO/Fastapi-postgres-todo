from dataclasses import dataclass

from src.exceptions import ApplicationException


@dataclass(eq=False)
class AuthorDoesNotExist(ApplicationException):
    author_id: int

    @property
    def message(self):
        return f'Author with id "{self.author_id}" does not exist'
