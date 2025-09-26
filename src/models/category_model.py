from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    # products: list[Product] = []
    # class Config:
    #     orm_mode = True