from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

users = [
    {"id": 1, "name": "Anna", "age": 25},
    {"id": 2, "name": "Alex", "age": 31},
]

app = FastAPI()


# get all
@app.get("/users")
def get_users():
    return users


class UserCreate(BaseModel):
    name: str
    age: int


@app.get("/users/filter")
def filter_users(user_age: int = None, user_name: str = None):
    result = []

    for user in users:
        if user_age is not None and user["age"] != user_age:
            continue

        if user_name is not None and user_name.lower() not in user["name"].lower():
            continue

        result.append(user)

    return result


# get id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


# Post - create
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age,
    }

    users.append(new_user)

    return new_user


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None


# Patch - update one field
@app.patch("/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    for user in users:
        if user["id"] == user_id:
            if user_data.name is not None:
                user["name"] = user_data.name

            if user_data.age is not None:
                user["age"] = user_data.age

            return user

    raise HTTPException(status_code=404, detail="User not found")


# Delete
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return

    raise HTTPException(status_code=404, detail="User not found")
