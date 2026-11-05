from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import select

engine = create_engine("sqlite:///sqlalchemy_intro/sqlalchemy.db")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]


Base.metadata.create_all(engine)


with Session(engine) as session:
    user = User(name="Anna", age=25)

    session.add(user)
    session.commit()


with Session(engine) as session:
    statement = select(User)

    users = session.scalars(statement).all()

    for user in users:
        print(user.id, user.name, user.age)


with Session(engine) as session:
    statement = select(User).where(User.id == 1)

    user = session.scalar(statement)

    if user is not None:
        print(user.id, user.name, user.age)
    else:
        print("User not found")


with Session(engine) as session:
    statement = select(User).where(User.id == 1)

    user = session.scalar(statement)

    if user is not None:
        user.age = 26
        session.commit()

        print("After update:", user.id, user.name, user.age)
    else:
        print("User not found")


with Session(engine) as session:
    statement = select(User).where(User.id == 2)

    user = session.scalar(statement)

    if user is not None:
        session.delete(user)
        session.commit()

        print("User deleted")

    statement = select(User)
    users = session.scalars(statement).all()

    for user in users:
        print(user.id, user.name, user.age)
