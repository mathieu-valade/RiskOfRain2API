from django.db import models
from .achievement import Achievement


class Character(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    health = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)
    achievement = models.ForeignKey(Achievement,
                                    on_delete=models.CASCADE,
                                    null=True)
