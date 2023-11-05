from pathlib import Path
from .ConfigEnv import ConfigEnv
from django.db import connection


class ConfigDB():
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir

    def get_db_config(self, base_dir: Path) -> dict[str, dict[str, str | Path | None | dict[str, str | None]]]:
        db_config = ConfigEnv.get_instance().db_config

        if db_config is None:
            return {
                "default": {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': base_dir / 'db.sqlite3',
                }
            }
        return {
            "default": {
                "ENGINE": db_config.engine,
                "NAME": db_config.database_name,
                "USER": db_config.user_name,
                "PASSWORD": db_config.password or '',
                "HOST": db_config.host,
                "PORT": db_config.port or '',
                'OPTIONS': {
                    'driver': 'ODBC Driver 17 for SQL Server',
                },
            }
        }

    def connect_to_database(self, db_config: dict[str, dict[str, str | Path | None | dict[str, str | None]]]):
        try:
            connection.ensure_connection()
            print("Connected to DB successfully")
        except Exception as e:
            print("Error connecting to DB")
            print("Fallback to SQLite3 database.")
            db_config['default']['ENGINE'] = 'django.db.backends.sqlite3'
            db_config['default']['NAME'] = self.base_dir / 'db.sqlite3'
            db_config['default']['USER'] = ''
            db_config['default']['PASSWORD'] = ''
            db_config['default']['HOST'] = ''
            db_config['default']['PORT'] = ''
            db_config['default']['OPTIONS'] = {}
