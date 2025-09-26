from sqlalchemy.orm import Session
from src.entities.product_entity import Product

def get_all_products(db: Session):
    return db.query(Product).all()