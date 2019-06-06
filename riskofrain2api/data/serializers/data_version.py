from rest_framework import serializers
from riskofrain2api.data.models import DataVersion


class DataVersionSerializer(serializers.ModelSerializer):
    command = serializers.CharField()
    date = serializers.DateTimeField(format='%Y%m%d%H%M%S', required=False)

    class Meta:
        model = DataVersion
        fields = ['command', 'date']
