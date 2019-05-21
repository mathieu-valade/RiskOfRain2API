from rest_framework import viewsets
from riskofrain2api.data.serializers import AchievementSerializer
from riskofrain2api.data.models import Achievement


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']
