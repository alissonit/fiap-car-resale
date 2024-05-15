from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    db_uri: Optional[str]
    db_max_pool_size: int = 5

    class Config:
        env_prefix = 'DB_'
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_insensitive = True


@lru_cache
def get_db_settings(env: Optional[str] = None) -> DBSettings:
    if env is None:
        return DBSettings()
    return DBSettings(_env_file=f".env.{env}")
