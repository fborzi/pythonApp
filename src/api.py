from fastapi import FastAPI
from src.controllers.product_controller import router as products_router
from src.controllers.category_controller import router as categories_router

def register_routes(app: FastAPI):
    app.include_router(products_router)
    app.include_router(categories_router)