from rest_framework import serializers
from riskofrain2api.data.models import DataVersion


class DataVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataVersion
        fields = ['date']
