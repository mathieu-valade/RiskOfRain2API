from rest_framework import serializers
from riskofrain2api.data.models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('icon', 'name', 'description', 'cooldown', 'character')
