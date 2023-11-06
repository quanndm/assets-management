from django.db import models


class StatusAsset(models.Model):
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.status
