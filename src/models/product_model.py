from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    category_id: int

    # class Config:
    #     orm_mode = True