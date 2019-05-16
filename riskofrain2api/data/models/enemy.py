from django.db import models


class Enemy(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    health = models.CharField(max_length=64)
    damage = models.CharField(max_length=64)
