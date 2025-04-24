from pydantic import BaseModel, Field, ConfigDict


class SGoods(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field()
    name: str = Field()
    description: str = Field()
    price: int = Field(ge=0)
    categoryId: int = Field()