from rest_framework import serializers
from riskofrain2api.data.models import Item


class ItemSerializer(serializers.ModelSerializer):
    achievement_name = serializers.ReadOnlyField(source='achievement.name')

    class Meta:
        model = Item
        fields = ('icon', 'name', 'description', 'achievement_name')
