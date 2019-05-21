from rest_framework import viewsets
from riskofrain2api.data.serializers import LevelSerializer
from riskofrain2api.data.models import Level


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    http_method_names = ['get']
