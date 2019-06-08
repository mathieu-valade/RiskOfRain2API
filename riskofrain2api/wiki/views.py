from rest_framework import viewsets
from rest_framework.response import Response
from riskofrain2api.wiki.build import (
    get_stats,
    get_achievements,
)


class BuildViewSet(viewsets.ViewSet):

    def create(self, request):
        item_list = request.data

        stat_list = []
        achievement_list = []

        for key, value in item_list.items():
            stat = get_stats(key, int(value))
            if stat is not None:
                stat_list.append(stat)
            achievement = get_achievements(key)
            if achievement is not None:
                achievement_list.append(achievement)

        return Response({"stats": stat_list, "achievements": achievement_list})
