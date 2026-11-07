from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pwdlib import PasswordHash

app = FastAPI()

SECRET_KEY = "40c4b3ad1b95f4f087d0e12e96f2e494e1e4ab32914dbe34e57fa6488fa9a12c"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()


class LoginData(BaseModel):
    email: str
    password: str


fake_user = {
    "id": 5,
    "email": "anna@example.com",
    "hashed_password": password_hash.hash("123456"),
}


def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    data = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/login")
def login(login_data: LoginData):
    if login_data.email != fake_user["email"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    password_is_correct = password_hash.verify(
        login_data.password, 
        fake_user["hashed_password"]
    )

    if not password_is_correct:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(fake_user["id"])

    return {"access_token": token, "token_type": "bearer"}
