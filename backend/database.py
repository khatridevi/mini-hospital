import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
database_url = os.getenv("DATABASE_URL", "sqlite:///./hospital.db")

engine = create_engine(database_url, connect_args={"check_same_thread": False} if "sqlite" in database_url else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()