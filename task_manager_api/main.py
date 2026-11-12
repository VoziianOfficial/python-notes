from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base
from models import Task, User
from sqlalchemy.orm import Session
from schemas import UserCreate, LoginData, TaskCreate, TaskUpdate
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select

app = FastAPI()
security = HTTPBearer()


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


@app.post("/login")
def login_user(login_data: LoginData):
    with Session(engine) as session:
        statement = select(User).where(User.email == login_data.email)
        user = session.scalar(statement)

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        password_is_correct = verify_password(
            login_data.password,
            user.hashed_password
        )
        if password_is_correct is False:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token(user.id, user.role)

        return {
            "access_token": token,
            "token_type": "bearer"
        }


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
    )

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    user_id = int(user_id)

    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.scalar(statement)

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user


@app.get("/profile")
def get_profile(current_user:User = Depends(get_current_user)):
   return {
       "id": current_user.id,
       "email": current_user.email,
       "role": current_user.role
   }


@app.post("/tasks")
def create_task(task_data: TaskCreate,
    current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        new_task = Task(
            title = task_data.title,
            user_id = current_user.id
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        return {
            "id": new_task.id,
            "title": new_task.title,
            "completed": new_task.completed,
            "user_id": new_task.user_id,
        }


@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        statement = select(Task).where(Task.user_id == current_user.id)
        user_tasks = session.scalars(statement).all()

        return user_tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
        task = session.scalar(statement)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        return task



@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
        task = session.scalar(statement)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        if task_data.title is not None:
            task.title = task_data.title
        if task_data.completed is not None:
            task.completed = task_data.completed

        session.commit()
        session.refresh(task)

        return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
        task = session.scalar(statement)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        session.delete(task)
        session.commit()

        return {"detail": "Task deleted successfully"}