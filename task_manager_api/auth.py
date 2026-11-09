from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()

SECRET_KEY = "0196bed1becf5a77c20120aebff9d971bbc6d54c91a020f42c50e10f30413ae2"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    data = {
        "sub": str(user_id),
        "role": role,
        "exp": expire,
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.InvalidTokenError:
        return None
