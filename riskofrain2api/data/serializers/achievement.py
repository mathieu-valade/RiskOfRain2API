from rest_framework import serializers
from riskofrain2api.data.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('icon', 'name', 'description')
