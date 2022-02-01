from sqlalchemy import (
    Column,
    String
)
from src.database import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    sub = Column(String(36), primary_key=True)
