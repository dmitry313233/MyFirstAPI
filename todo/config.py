import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = os.getenv('NAME_APP')   # Pydentic требует указать тип str, иначе будет ошибка   передаётся в html
    db_url: str = os.getenv('SQLALCHEMY_DATABASE_URL')  # Pydentic требует указать тип str, иначе будет ошибка

    class Config:
        env_file: str = '../.env'


settings = Settings()
