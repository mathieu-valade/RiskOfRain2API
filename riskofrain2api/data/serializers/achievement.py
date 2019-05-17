from rest_framework import serializers
from ..models.achievement import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('name', 'description')
