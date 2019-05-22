from rest_framework import viewsets
from riskofrain2api.data.serializers import DataVersionSerializer
from riskofrain2api.data.models import DataVersion


class DataVersionViewSet(viewsets.ModelViewSet):
    queryset = DataVersion.objects.all()
    serializer_class = DataVersionSerializer
    http_method_names = ['get']
