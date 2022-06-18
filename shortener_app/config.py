# shortener_app/config.py
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "ec2-34-198-186-145.compute-1.amazonaws.com"
    db_url: str = "postgres://ystvatsjikzagi:e0b4e33a0d687506bb6e04fd9f44e0c5efd08215f1c77331db6e227f28462aee@ec2-34-198-186-145.compute-1.amazonaws.com:5432/de6jsbsjhk0gh6"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings


get_settings().db_url
