class EmailConfigInfo():
    host: str | None
    port: str | int | None
    user: str | None
    password: str | None
    use_tls: bool | str | None
    backend: str | None

    def __init__(self,
                 host: str | None = None,
                 port: str | int | None = None,
                 user: str | None = None,
                 password: str | None = None,
                 use_tls: bool | str | None = None,
                 backend: str | None = None
                 ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.use_tls = use_tls
        self.backend = backend
