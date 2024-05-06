from dataclasses import dataclass

from src.core.exceptions import ApplicationException


@dataclass(eq=False)
class AuthorDoesNotExist(ApplicationException):
    author_id: int

    @property
    def message(self):
        return f'Author with id \'{self.author_id}\' does not exist'


@dataclass(eq=False)
class TaskDoesNotExist(ApplicationException):
    task_id: int

    @property
    def message(self):
        return f'Task with id \'{self.task_id}\' does not exist'
