from rest_framework import viewsets
from riskofrain2api.data.serializers import DataVersionSerializer
from rest_framework.response import Response
from riskofrain2api.data.models import DataVersion

from riskofrain2api.data.data_access.data_version import (
    import_data,
    export_data,
)
from riskofrain2api.data.scraper.core import (
    clean_get_data,
    clear_data,
)


class DataVersionViewSet(viewsets.ModelViewSet):
    queryset = DataVersion.objects.all()
    serializer_class = DataVersionSerializer
    http_method_names = ['get', 'post']

    def create(self, request):
        body = request.body

        if 'command' in body:
            if body['command'] == 'update':
                clean_get_data()
                export_data()
            elif body['command'] == 'load':
                if 'target' in body:
                    import_data(body['target'])
            elif body['command'] == 'clear':
                clear_data()

        queryset = DataVersion.objects.all()
        serializer = DataVersionSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
