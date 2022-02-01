
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config import config


DB_URI = config.db_string

engine = create_engine(
    DB_URI
)

sm = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = sm()
SqlAlchemyBase = declarative_base()