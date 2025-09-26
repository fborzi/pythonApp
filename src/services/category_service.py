from sqlalchemy.orm import Session
from src.entities.category_entity import Category

def get_all_categories(db: Session):
    return db.query(Category).all()