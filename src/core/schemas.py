from pydantic import BaseModel, ConfigDict


class CustomBaseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra='ignore')


class BaseOutSchema(BaseModel):
    id: int
