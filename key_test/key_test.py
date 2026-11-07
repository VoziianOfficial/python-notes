from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "40c4b3ad1b95f4f087d0e12e96f2e494e1e4ab32914dbe34e57fa6488fa9a12c"
ALGORITHM = "HS256"


def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    data = {
        "sub": str(user_id),
        "exp": expire,
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token


token = create_access_token(5)
print(token)


decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

print(decoded)
