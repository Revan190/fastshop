from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Any,
    Union,
)
import logging

from jose import jwt
from passlib.context import CryptContext

from src.base_settings import base_settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = logging.getLogger(__name__)


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None,
) -> str:
    try:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=base_settings.auth.access_token_expire_minutes,
            )
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, base_settings.auth.secret_key, algorithm=base_settings.auth.algorithm)
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error creating access token: {e}")
        raise


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
