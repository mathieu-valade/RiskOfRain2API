from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    AbilitySerializer,
    AchievementSerializer,
    CharacterSerializer,
    EnemySerializer,
    ItemSerializer,
    LevelSerializer
)

from .models import (
    Ability,
    Achievement,
    Character,
    Enemy,
    Item,
    Level
)

from .scrapper.core import get_data


@api_view(['POST'])
def scrap_data(request):
    get_data()

    return Response(status=200)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get']


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    http_method_names = ['get']


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    http_method_names = ['get']


class EnemyViewSet(viewsets.ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer
    http_method_names = ['get']


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    http_method_names = ['get']
