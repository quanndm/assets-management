from django.db import models

from . import StatusAsset, Category, Supplier


class Asset(models.Model):
    name = models.CharField(max_length=256)
    serial_number = models.CharField(max_length=50)
    date_purchase = models.DateField()
    date_end_of_warranty = models.DateField()
    status = models.ForeignKey(
        StatusAsse-t, on_delete=models.CASCADE)  # type: ignore
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)  # type: ignore
    value = models.IntegerField()
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)  # type: ignore
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
