from rest_framework import viewsets
from riskofrain2api.data.serializers import ItemSerializer
from riskofrain2api.data.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get']
