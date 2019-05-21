from rest_framework import serializers
from riskofrain2api.data.models import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name', 'title', 'description')
