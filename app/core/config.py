from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',env_file_encoding='utf-8',extra='ignore')
    app_name:str='Community AI Backend'
    environment:str='development'
    api_prefix:str='/api/v1'
    database_url:str='postgresql+asyncpg://app:app@postgres:5432/app'
    redis_url:str='redis://redis:6379/0'
    llm_provider:str='mock'
    llm_base_url:str='https://api.openai.com/v1'
    llm_api_key:str=''
    llm_model:str='gpt-4.1-mini'
    cors_origins:list[str]=Field(default_factory=lambda:['http://localhost:3000'])
    request_timeout_seconds:float=30.0
    docs_enabled:bool=True

@lru_cache
def settings()->Settings:return Settings()

# Backwards-compatible alias
def get_settings()->Settings:
    return settings()
