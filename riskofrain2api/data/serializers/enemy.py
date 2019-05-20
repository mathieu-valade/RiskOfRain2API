from rest_framework import serializers
from ..models.enemy import Enemy


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ('icon', 'name', 'health', 'damage')
