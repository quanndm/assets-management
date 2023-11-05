class DBConfigInfo():
    host: str | None
    port: str | None
    database_name: str | None
    user_name: str | None
    password: str | None
    driver: str | None
    engine: str | None

    def __init__(self,
                 host: str | None = None,
                 port: str | None = None,
                 database_name: str | None = None,
                 user_name: str | None = None,
                 password: str | None = None,
                 driver: str | None = None,
                 engine: str | None = None
                 ):
        self.host = host
        self.port = port
        self.database_name = database_name
        self.user_name = user_name
        self.password = password
        self.driver = driver
        self.engine = engine
