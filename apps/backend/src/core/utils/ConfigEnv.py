import os
from dotenv import load_dotenv

from ..dtos import DBConfigInfo


class ConfigEnv:
    db_config: DBConfigInfo.DBConfigInfo | None = None

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Database configuration
        self.db_config = DBConfigInfo.DBConfigInfo(
            port=os.getenv('DB_PORT'),
            host=os.getenv('DB_HOST'),
            database_name=os.getenv('DB_NAME'),
            user_name=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            driver=os.getenv('DB_DRIVER'),
            engine=os.getenv('DB_ENGINE')
        )
        if self.db_config.host is None:
            self.db_config = None

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance
