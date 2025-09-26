import os
from dotenv import load_dotenv
from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

URL_DATABASE = os.getenv("DATABASE_URL")

if URL_DATABASE is None:
    raise ValueError("DATABASE_URL environment variable is not set")
else:
    engine = create_engine(URL_DATABASE)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
