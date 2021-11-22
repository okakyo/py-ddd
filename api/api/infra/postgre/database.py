from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ["DB_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(
  autocommit=False,
  utoflush=False,
  bind=engine
)

DbBase = declarative_base()

def create_tables():
  DbBase.metadata.create_all(bind=engine)
