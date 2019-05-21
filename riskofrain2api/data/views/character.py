from rest_framework import viewsets
from riskofrain2api.data.serializers import CharacterSerializer
from riskofrain2api.data.models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    http_method_names = ['get']
