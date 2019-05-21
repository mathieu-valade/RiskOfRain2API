from rest_framework import viewsets
from riskofrain2api.data.serializers import EnemySerializer
from riskofrain2api.data.models import Enemy


class EnemyViewSet(viewsets.ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer
    http_method_names = ['get']
