import os
from dotenv import load_dotenv

from ..dtos import DBConfigInfo, EmailConfigInfo, AdminInfo


class ConfigEnv:
    db_config: DBConfigInfo.DBConfigInfo | None = None
    email_config: EmailConfigInfo.EmailConfigInfo | None = None
    secret_key: str | None = None

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
        if self.db_config.host == "":
            self.db_config = None

        # Email configuration
        self.email_config = EmailConfigInfo.EmailConfigInfo(
            host=os.getenv('EMAIL_HOST'),
            port=os.getenv('EMAIL_PORT'),
            user=os.getenv('EMAIL_HOST_USER'),
            password=os.getenv('EMAIL_HOST_PASSWORD'),
            use_tls=os.getenv('EMAIL_USE_TLS') or False,
            backend=os.getenv('EMAIL_BACKEND')
        )

        # Secret key
        self.secret_key = os.getenv('SECRET_KEY')

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance
