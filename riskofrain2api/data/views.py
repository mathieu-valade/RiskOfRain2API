from rest_framework import viewsets
from riskofrain2api.data.models import (
    Item,
    Achievement,
    Character,
    Ability,
    Enemy,
    Level
)

from riskofrain2api.data.serializers import (
    ItemSerializer,
    AchievementSerializer,
    CharacterSerializer,
    AbilitySerializer,
    EnemySerializer,
    LevelSerializer
)


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
