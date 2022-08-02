import decouple
from loguru import logger


class Settings:
    API_TOKEN = decouple.config("API_TOKEN")
    ADMIN = decouple.config("ADMIN")

    PG_NAME = decouple.config("PG_NAME")
    PG_HOST = decouple.config("PG_HOST")
    PG_PORT = decouple.config("PG_PORT")
    PG_USER = decouple.config("PG_USER")
    PG_PASSWORD = decouple.config("PG_PASSWORD")

    @classmethod
    def get_db_connection_data(cls):
        return {k[3:].lower(): v for k, v in cls.__dict__.items() if k[:3] == "PG_"}


settings = Settings()
logger.info(settings.get_db_connection_data())
