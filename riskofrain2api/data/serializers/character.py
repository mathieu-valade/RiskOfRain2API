from rest_framework import serializers
from ..models.character import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('icon', 'name', 'health', 'description')
