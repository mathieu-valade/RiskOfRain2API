"""riskofrain2api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from riskofrain2api.data.views import (
    ItemViewSet,
    AchievementViewSet,
    CharacterViewSet,
    AbilityViewSet,
    EnemyViewSet,
    LevelViewSet,
    DataVersionViewSet
)
from riskofrain2api.wiki.views import (
    BuildViewSet
)


ROUTER = routers.DefaultRouter()
ROUTER.register('items', ItemViewSet)
ROUTER.register('achievements', AchievementViewSet)
ROUTER.register('characters', CharacterViewSet)
ROUTER.register('abilities', AbilityViewSet)
ROUTER.register('enemies', EnemyViewSet)
ROUTER.register('levels', LevelViewSet)
ROUTER.register('dataversions', DataVersionViewSet)
ROUTER.register('build', BuildViewSet, basename='build')


SCHEMA_VIEW = get_schema_view(
   openapi.Info(
      title="RiskOfRain2 API",
      default_version='v1',
      description="Risk Of Rain 2 wiki as an API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path(r'swagger.yaml', SCHEMA_VIEW.without_ui(cache_timeout=0),
         name='schema-json'),
    path(r'swagger/', SCHEMA_VIEW.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
]

FAILING = 'this is a very long sentence and it might just go over the column limit by mistake asdasd'
