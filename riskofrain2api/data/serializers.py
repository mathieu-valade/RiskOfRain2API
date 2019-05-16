from rest_framework import serializers
from .models.ability import Ability
from .models.achievement import Achievement
from .models.character import Character
from .models.enemy import Enemy
from .models.item import Item
from .models.level import Level


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('name', 'description')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('icon', 'name', 'description', 'achievement')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('icon', 'name', 'health', 'description')


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('icon', 'description', 'cooldown', 'character')


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ('icon', 'name', 'health', 'damage')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name', 'title', 'description')
