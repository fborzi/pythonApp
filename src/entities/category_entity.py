from sqlalchemy.types import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.entities.base import Base

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    