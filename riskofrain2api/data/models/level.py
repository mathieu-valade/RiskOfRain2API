from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
