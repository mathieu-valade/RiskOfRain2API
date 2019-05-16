from django.db import models


class Achievement(models.Model):
    icon = models.CharField(max_length=512)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)
