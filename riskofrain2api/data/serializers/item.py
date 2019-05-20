from rest_framework import serializers
from ..models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('icon', 'name', 'description', 'achievement')
