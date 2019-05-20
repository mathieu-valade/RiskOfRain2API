from django.db import models
from .character import Character


class Ability(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)
    cooldown = models.CharField(max_length=32)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
