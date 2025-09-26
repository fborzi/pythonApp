from fastapi import APIRouter
from src.database.dbconfig import db_dependency
from src.services.product_service import get_all_products


router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.get("")
async def read_products(db: db_dependency):
    return get_all_products(db)