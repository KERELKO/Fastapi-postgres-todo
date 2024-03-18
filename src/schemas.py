from enum import Enum

from pydantic import BaseModel, ConfigDict


class Status(Enum):
    COMPLETED = 'COMPLETED'
    UNCOMPLETED = 'UNCOMPLETED'


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')
