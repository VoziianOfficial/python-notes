from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str



class LoginData(BaseModel):
    email: str
    password: str


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None