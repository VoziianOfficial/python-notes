from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///sqlalchemy_intro/sqlalchemy.db")

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    orders: Mapped[list["Order"]] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    product: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")

Base.metadata.create_all(engine)


class UserCreate(BaseModel):
    name: str
    age: int


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None


class OrderCreate(BaseModel):
    product: str
    user_id: int


app = FastAPI()


@app.get("/users")
def get_users():
    with Session(engine) as session:
        statement = select(User)

        users = session.scalars(statement).all()

        result = []

        for user in users:
            result.append(
                {
                    "id": user.id,
                    "name": user.name,
                    "age": user.age,
                }
            )

        return result


@app.get("/users/{user_id}")
def get_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)

        user = session.scalar(statement)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
        }


@app.post("/users", status_code=201)
def create_user(user_data: UserCreate):
    with Session(engine) as session:
        
        user = User(name=user_data.name, age=user_data.age)

        session.add(user)
        session.commit()

        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
        }


@app.patch("/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)

        user = session.scalar(statement)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user_data.name is not None:
            user.name = user_data.name

        if user_data.age is not None:
            user.age = user_data.age

        session.commit()

        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
        }


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)

        user = session.scalar(statement)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        session.delete(user)
        session.commit()


@app.post("/orders", status_code=201)
def create_order(order_data: OrderCreate):
    with Session(engine) as session:
        statement = select(User).where(User.id == order_data.user_id)
        user = session.scalar(statement)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        order = Order(
            product=order_data.product, 
            user_id=order_data.user_id)

        session.add(order)
        session.commit()

        return {
            "id": order.id,
            "product": order.product,
            "user_id": order.user_id,
        }


@app.get("/orders")
def get_orders():
    with Session(engine) as session:
        statement = select(Order)

        orders = session.scalars(statement).all()

        result = []

        for order in orders:
            result.append(
                {
                    "id": order.id,
                    "product": order.product,
                    "user_id": order.user_id,
                }
            )

        return result


@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int):
    with Session(engine) as session:
        user = session.scalar(select(User).where(User.id == user_id))

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")


        result = []

        for order in user.orders:
            result.append(
                {
                    "id": order.id,
                    "product": order.product,
                    "user_id": order.user_id,
                }
            )

        return result
