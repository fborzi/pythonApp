from sqlalchemy.orm import Session
from src.schemas.product_schema import ProductCreate, ProductUpdate
from src.entities.product_entity import Product

def create_new_product(db: Session,
                       product: ProductCreate):
    new_product = Product(
        name = product.name,
        description = product.description,
        price = product.price,
        is_available = product.is_available,
        category_id = product.category_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product_by_id(db: Session, product_id: int, 
                         product_update: ProductUpdate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        product.name = product_update.name or product.name
        product.description = product_update.description or product.description
        product.price = product_update.price or product.price
        product.is_available = product_update.is_available if product_update.is_available is not None else product.is_available
        product.category_id = product_update.category_id if product_update.category_id is not None else product.category_id
        db.commit()
        db.refresh(product)
        return product
    return None

def delete_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False