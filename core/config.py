from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str
    POSTGRES_USER : str 
    POSTGRES_PASSWORD : str
    POSTGRES_PORT : int = 5432
    POSTGRES_DB : str 

    OPENROUTERAPIKEY : str
    HUGGINGFACEAPIKEY : str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()


