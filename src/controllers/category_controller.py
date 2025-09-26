from fastapi import APIRouter
from src.database.dbconfig import db_dependency
from src.services.category_service import get_all_categories


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.get("")
async def read_categories(db: db_dependency):
    return get_all_categories(db)