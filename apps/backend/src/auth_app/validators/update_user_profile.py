from datetime import datetime
from django.contrib.auth.models import User
from ..types.gender_enum import Gender


def update_user_profile(data: dict[str, str | None], pk: int) -> tuple[bool, list[str]]:
    format = "%Y-%m-%d"
    errors: list[str] = []

    # ----start validate---------------
    # get all user except current user
    user = User.objects.exclude(pk=pk, email=data["email"])
    if user.filter(username=data["user_name"]).exists():
        errors.append("This username is already in use")

    # if user.filter(email=data["email"]).exists():
    #     errors.append("This email is already in use")

    if data["gender"] not in (Gender.MALE.value, Gender.FEMALE.value):
        errors.append("Gender Must be M or F")

    # validate birth date
    if not data["date_of_birth"] or data["date_of_birth"] == "":
        errors.append("date of birth cannot be blank")

    try:
        bool(datetime.strptime(data["date_of_birth"] or '', format))
    except:
        errors.append("Birthdate must be formatted correctly: yyyy-mm-dd")

    if len(errors) > 0:
        return (False, errors)
    return (True, [])
