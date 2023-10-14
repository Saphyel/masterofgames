# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    steam_api_key: str
    steam_url: str = "https://api.steampowered.com"


config = Config()
