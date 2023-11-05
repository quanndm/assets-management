from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    note = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
