from typing import Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class MongoSettings(BaseModel):
    url: str = 'mongodb://mongo-db:27017/fastshop'
    direct_connection: bool = False
    const_status_prepared: str = 'prepared'

class PostgresSettings(BaseModel):
    user: str = 'user'
    password: str = 'password'
    db: str = 'fastapi_shop'
    host: str = 'db'
    port: int = 5432
    url: str = 'postgresql+asyncpg://user:password@db:5432/fastapi_shop'

class AuthorizationSettings(BaseModel):
    secret_key: str = 'default_secret_key'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = Field(default=30, gt=0)
    crypt_schema: str = 'bcrypt'

class ProjectSettings(BaseSettings):
    api_key: str = "default_api_key"
    debug: Optional[bool] = True
    api_logger_format: Optional[str] = '%(levelname)s: %(asctime)s - %(message)s'

    postgres: PostgresSettings = PostgresSettings()
    auth: AuthorizationSettings = AuthorizationSettings()
    mongo: MongoSettings = MongoSettings()

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        frozen=True,
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

base_settings = ProjectSettings()
