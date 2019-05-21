from django.db import models
from riskofrain2api.data.models import Achievement


class Item(models.Model):
    icon = models.CharField(max_length=512)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)
    achievement = models.ForeignKey(Achievement,
                                    on_delete=models.CASCADE,
                                    null=True)
