from django.db import models
from django.contrib.auth.models import User
from ..types.gender_enum import Gender
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, default="")
    gender = models.CharField(max_length=1, blank=True,
                              null=True, default=Gender.MALE.value)
    is_admin = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    avatar = models.CharField(
        max_length=500, blank=True, null=True, default="")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, default="")

    def __str__(self):
        return self.user.username
