from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from pwdlib import PasswordHash

app = FastAPI()


SECRET_KEY = "40c4b3ad1b95f4f087d0e12e96f2e494e1e4ab32914dbe34e57fa6488fa9a12c"
ALGORITHM = "HS256"

security = HTTPBearer()
password_hash = PasswordHash.recommended()


class LoginData(BaseModel):
    email: str
    password: str


fake_user = {
    "id": 5,
    "email": "anna@example.com",
    "hashed_password": password_hash.hash("123456"),
}


# Создаём JWT
def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    data = {
        "sub": str(user_id),
        "exp": expire,
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token


# Login
@app.post("/login")
def login(login_data: LoginData):

    if login_data.email != fake_user["email"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    password_is_correct = password_hash.verify(
        login_data.password, fake_user["hashed_password"]
    )

    if not password_is_correct:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(fake_user["id"])

    return {"access_token": token, "token_type": "bearer"}


# Проверяем JWT и достаём user_id
def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return int(user_id)

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# Защищённый endpoint
@app.get("/profile")
def get_profile(user_id: int = Depends(get_current_user_id)):
    return {"user_id": user_id, "message": "You are authenticated"}
