from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    category_id: int

    model_config = ConfigDict(from_attributes=True)