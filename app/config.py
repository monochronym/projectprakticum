# import os
# from pydantic_settings import BaseSettings, SettingsConfigDict
# import redis
#
# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_NAME: str
#     DB_USER: str
#     DB_PASSWORD: str
#     SECRET_KEY: str
#     ALGORITHM: str
#     REDIS_HOST: str
#     REDIS_PORT: str
#     REDIS_PASSWORD: str
#     model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))
#
#
# settings = Settings()
#
#
# def get_db_url():
#     return (
#         f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
#
def get_auth_data():
    return {"algorithm": "HS256", "secret_key":"gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt"}
#
# redis_client = redis.Redis(host=settings.REDIS_HOST,
#                            port=settings.REDIS_PORT,
#                            username="default",
#                            password=settings.REDIS_PASSWORD,
#                            db=0)
# redis.Redis(host='localhost', port=6379, db=0, username='default', password='CasperTo360Flip')