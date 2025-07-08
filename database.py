from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+pg8000://postgres:xina@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)
