from rest_framework import viewsets
from rest_framework.response import Response
from riskofrain2api.wiki.build import get_stats


class BuildViewSet(viewsets.ViewSet):

    def create(self, request):
        item_list = request.data

        stat_list = []

        for key, value in item_list.items():
            stat = get_stats(key, value)
            if stat is not None:
                stat_list.append(stat)

        return Response(stat_list)