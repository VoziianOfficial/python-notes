from fastapi import FastAPI, HTTPException
from database import engine, Base
from models import Task, User
from sqlalchemy.orm import Session
from schemas import UserCreate
from auth import hash_password
from sqlalchemy import select

app = FastAPI()


Base.metadata.create_all(engine)



@app.post("/register")
def register_user(user_data: UserCreate):
    with Session(engine) as session:
        statement = select(User).where(User.email == user_data.email)
        existing_user = session.scalar(statement)
        if existing_user is not None:
            raise HTTPException(status_code=409, detail="Email already registered")

        hashed_password = hash_password(user_data.password)

        new_user = User(
            email = user_data.email,
            hashed_password = hashed_password,
            role = 'user'
        )

        session.add(new_user)
        session.commit()

        return {
            "id": new_user.id,
            "email": new_user.email,
            "role": new_user.role,
        }


