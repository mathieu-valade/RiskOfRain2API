from rest_framework import viewsets
from riskofrain2api.data.serializers import AbilitySerializer
from riskofrain2api.data.models import Ability


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    http_method_names = ['get']
