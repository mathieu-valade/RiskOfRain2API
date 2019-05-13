from rest_framework import serializers
from riskofrain2api.data.models import Achievement, Item

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('name', 'description')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('icon', 'name', 'description', 'achievement')