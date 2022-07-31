import decouple
from loguru import logger


class Settings:
    API_TOKEN = decouple.config("TELEGRAM_API_TOKEN")

    PG_DB = decouple.config("DB_NAME")
    PG_HOST = decouple.config("DB_HOST")
    PG_PORT = decouple.config("DB_PORT")
    PG_USER = decouple.config("DB_USER")
    PG_PASSWORD = decouple.config("DB_PASSWORD")

    @classmethod
    def get_db_connection_data(cls):
        return {k[3:].lower(): v for k, v in cls.__dict__.items() if k[:3] == 'PG_'}


settings = Settings()
logger.info(settings.get_db_connection_data())
