from fastapi import APIRouter
from src.schemas.product_schema import ProductCreate, ProductOut, ProductUpdate
from src.database.dbconfig import db_dependency
from src.services.product_service import (create_new_product, 
                                          delete_product_by_id, 
                                          get_all_products, 
                                          get_product_by_id, 
                                          update_product_by_id)


router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.post("/create", response_model=ProductOut, status_code=201)
async def create_product(db: db_dependency, payload: ProductCreate):
    return create_new_product(db, payload)

@router.get("")
async def read_products(db: db_dependency):
    return get_all_products(db)

@router.get("/{product_id}")
async def read_product(product_id: int, db: db_dependency):
    return get_product_by_id(db, product_id)

@router.put("/update/{product_id}")
async def update_product(product_id: int, 
                          payload: ProductUpdate, 
                          db: db_dependency):
    return update_product_by_id(db, product_id, payload)

@router.delete("/delete/{product_id}")
async def delete_product(product_id: int, db: db_dependency):
    return delete_product_by_id(db, product_id)