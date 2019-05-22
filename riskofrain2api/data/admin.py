# from django.contrib import admin

# Register your models here.
from import_export import resources
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
        fields = ('icon', 'name', 'description', 'cooldown', 'character__name')


class AchievementResource(resources.ModelResource):
    class Meta:
        model = Achievement
        fields = ('icon', 'name', 'description')


class CharacterResource(resources.ModelResource):
    class Meta:
        model = Character
        fields = ('icon', 'name', 'health', 'achievement__name')


class EnemyResource(resources.ModelResource):
    class Meta:
        model = Enemy
        fields = ('icon', 'name', 'health', 'damage')


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        fields = ('icon', 'name', 'description', 'achievement__name')


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level
        fields = ('name', 'title', 'description')
