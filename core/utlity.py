from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from fastapi.concurrency import run_in_threadpool

_ph = PasswordHasher()

DUMMY_HASH = _ph.hash("dummy-password-for-timing-only")


def _hash(password: str) -> str:
    return _ph.hash(password)


def _verify(password: str, hashed: str) -> bool:
    try:
        return _ph.verify(hashed, password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False


async def hash_password(password: str) -> str:
    return await run_in_threadpool(_hash, password)


async def verify_password(password: str, hashed: str) -> bool:
    return await run_in_threadpool(_verify, password, hashed)
