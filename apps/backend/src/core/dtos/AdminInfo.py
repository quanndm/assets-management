class AdminInfo():
    username: str | None
    password: str | None
    email: str | None

    def __init__(self, username: str | None, password: str | None, email: str | None) -> None:
        self.username = username
        self.password = password
        self.email = email
