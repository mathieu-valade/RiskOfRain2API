from django.db import models
from riskofrain2api.data.models import Achievement


class Character(models.Model):
    icon = models.CharField(max_length=512)
    name = models.CharField(max_length=64, unique=True)
    health = models.CharField(max_length=32)
    achievement = models.ForeignKey(Achievement,
                                    on_delete=models.CASCADE,
                                    null=True)
