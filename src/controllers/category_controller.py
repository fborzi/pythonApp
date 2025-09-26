from typing import Annotated
from fastapi import APIRouter, Body
from src.database.dbconfig import db_dependency
from src.services.category_service import (
    create_new_category, 
    get_all_categories, 
    delete_category_by_id, 
    get_category_by_id, 
    update_category_by_name
)

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.post("/create", status_code=201)
async def create_category(name: Annotated[str, Body(embed=True)], 
                          db: db_dependency):
    return create_new_category(db, name)

@router.get("")
async def read_categories(db: db_dependency):
    return get_all_categories(db)

@router.get("/{category_id}")
async def read_category(category_id: int, db: db_dependency):
    return get_category_by_id(db, category_id)

@router.put("/update/{category_name}")
async def update_category(category_name: str, 
                          name: Annotated[str, Body(embed=True)], 
                          db: db_dependency):
    return update_category_by_name(db, category_name, name)

@router.delete("/delete/{category_id}")
async def delete_category(category_id: int, db: db_dependency):
    return delete_category_by_id(db, category_id)