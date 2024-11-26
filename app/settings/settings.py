from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

import os


current_directory = os.path.dirname(os.path.abspath(__file__))
files_directory = os.path.abspath(
    os.path.join(current_directory, "../tmp/files")
)
scripts_directory = os.path.abspath(
    os.path.join(current_directory, "../scripts")
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="app/.env"
    )
    APP_NAME: str = "BASH SCRIPT TO JSON API"
    ADMIN_EMAIL: str = "admin@example.com"
    PER_PAGE: Optional[int] = 10
    PATH_FILES: str = files_directory
    PATH_SCRIPTS: str = scripts_directory


settings = Settings()

print("Configurações carregadas:")
print(settings.model_dump())
