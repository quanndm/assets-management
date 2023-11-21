def create_user_profile(data: dict[str, str | None]) -> tuple[bool, list[str]]:
    format = "%d-%m-%Y"
    errors: list[str] = []

    # ----start validate---------------
    if data["user_name"] is None or data["user_name"] == "":
        errors.append("Username cannot be blank")
    if data["last_name"] is None or data["last_name"] == "":
        errors.append("Last name cannot be blank")

    if data["first_name"] is None or data["first_name"] == "":
        errors.append("First name cannot be blank")

    if data["email"] is None or data["email"] == "":
        errors.append("Email cannot be blank")

    # return
    if len(errors) > 0:
        return (False, errors)
    return (True, [])
