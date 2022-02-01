from loguru import logger
from src.database import db_session
from src.database.user import User


class Seeder:

    def __init__(self):
        self.items = []

    def run(self):
        logger.info(f"Running seeder: {self.__class__.__name__}")
        db_session.add_all(self.items)
        logger.info(f"Inserting {len(self.items)} records")
        db_session.commit()
        logger.info(f"{self.__class__.__name__} seeding complete")


class DevUser(Seeder):
    def __init__(self):
        self.items = [
            User(
                sub="foo"
            ),
            User(
                sub="bar"
            )
        ]
