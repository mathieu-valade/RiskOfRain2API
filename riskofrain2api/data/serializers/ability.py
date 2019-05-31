from rest_framework import serializers
from riskofrain2api.data.models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    character_name = serializers.ReadOnlyField(source='character.name')

    class Meta:
        model = Ability
        fields = ('icon', 'name', 'description', 'cooldown', 'character_name')
