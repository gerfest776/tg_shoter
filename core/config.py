import decouple
from loguru import logger


class Settings:
    API_TOKEN = decouple.config("API_TOKEN", "test")
    ADMIN = decouple.config("ADMIN")

    PG_NAME = decouple.config("PG_NAME")
    APG_HOST = decouple.config("PG_HOST")
    PG_PORT = decouple.config("PG_PORT")
    APG_USER = decouple.config("PG_USER")
    APG_PASSWORD = decouple.config("PG_PASSWORD")

    @classmethod
    def get_db_connection_data(cls):
        return {k[4:].lower(): v for k, v in cls.__dict__.items() if k[:3] == "APG"}


settings = Settings()
logger.info(settings.get_db_connection_data())
