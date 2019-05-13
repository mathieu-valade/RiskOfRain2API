from django.db import models

# Create your models here.


class Achievement(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)


class Item(models.Model):
    icon = models.CharField(max_length=512)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)
    achievement = models.ForeignKey(Achievement,
                                    on_delete=models.CASCADE,
                                    null=True)


class Character(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    health = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)


class Ability(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=2048)
    cooldown = models.CharField(max_length=32)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)


class Enemy(models.Model):
    icon = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    health = models.CharField(max_length=64)
    damage = models.CharField(max_length=64)


class Level(models.Model):
    name = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
