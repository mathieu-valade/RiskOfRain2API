from rest_framework import serializers
from ..models.ability import Ability


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('icon','name', 'description', 'cooldown', 'character')
