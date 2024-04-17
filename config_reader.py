from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    API_KEY: SecretStr

    model_config = SettingsConfigDict(env_file='.venv/secret', env_file_encoding='utf-8')


config = Settings()