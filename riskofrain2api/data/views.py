from django.shortcuts import render
from rest_framework import viewsets
from riskofrain2api.data.models import Item
from riskofrain2api.data.serializers import ItemSerializer, AchievementSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get']

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']