# from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from riskofrain2api.data.models import (
    Ability,
    Achievement,
    Character,
    Enemy,
    Item,
    Level
)


class AbilityResource(resources.ModelResource):

    class Meta:
        model = Ability

        fields = ('icon', 'name', 'description', 'cooldown', 'character__id')


class AchievementResource(resources.ModelResource):
    class Meta:
        model = Achievement

        fields = ('icon', 'name', 'description')


class CharacterResource(resources.ModelResource):
    class Meta:
        model = Character

        fields = ('icon', 'name', 'health', 'achievement__id')


class EnemyResource(resources.ModelResource):
    class Meta:
        model = Enemy

        fields = ('icon', 'name', 'health', 'damage')


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

        fields = ('icon', 'name', 'description', 'achievement__id')


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level
        fields = ('name', 'title', 'description')
