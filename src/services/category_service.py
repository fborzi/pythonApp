from sqlalchemy.orm import Session
from src.entities.category_entity import Category

def create_new_category(db: Session, name: str):
    new_category = Category(name=name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category_by_name(db: Session, category_name: str, new_name: str):
    category = db.query(Category).filter(Category.name == category_name).first()
    if category:
        category.name = new_name
        db.commit()
        db.refresh(category)
        return category
    return None

def delete_category_by_id(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return True
    return False