import bcrypt


def hash_password(password: str) -> str:
    salt: bytes = bcrypt.gensalt()
    hashed_password: bytes = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
