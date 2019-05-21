from rest_framework import serializers
from riskofrain2api.data.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('icon', 'name', 'health', 'description')
