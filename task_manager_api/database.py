from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


engine = create_engine("sqlite:///task_manager_api/task_manager.db")


class Base(DeclarativeBase):
    pass