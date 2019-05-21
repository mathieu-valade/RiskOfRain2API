from rest_framework import serializers
from riskofrain2api.data.models import Enemy


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ('icon', 'name', 'health', 'damage')
