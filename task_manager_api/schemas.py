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


class UserResponse(BaseModel):
    id: int
    email: str
    role: str


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    user_id: int