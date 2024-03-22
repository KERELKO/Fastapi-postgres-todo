from enum import Enum


class Environment(str, Enum):
    PRODUCTION: str = 'PRODUCTION'
    LOCAL: str = 'LOCAL'
    TESTING: str = 'TESTING'

    @property
    def is_debug(self) -> bool:
        return self in (self.LOCAL, self.TESTING)

    @property
    def is_deployed(self) -> bool:
        return self in (self.PRODUCTION,)


DESCRIPTION = ''
