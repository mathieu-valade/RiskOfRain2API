from rest_framework import viewsets
from rest_framework.response import Response


from riskofrain2api.data.scraper.core import get_data


class ScraperViewSet(viewsets.ViewSet):

    def get(self, request):
        return Response(status=200)

    def create(self, request):
        get_data()
        return Response(status=200)
