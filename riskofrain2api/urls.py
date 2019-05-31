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
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from riskofrain2api.data.views import (
    ItemViewSet,
    AchievementViewSet,
    CharacterViewSet,
    AbilityViewSet,
    EnemyViewSet,
    LevelViewSet,
    DataVersionViewSet
)


ROUTER = routers.DefaultRouter()
ROUTER.register('items', ItemViewSet)
ROUTER.register('achievements', AchievementViewSet)
ROUTER.register('characters', CharacterViewSet)
ROUTER.register('abilities', AbilityViewSet)
ROUTER.register('enemies', EnemyViewSet)
ROUTER.register('levels', LevelViewSet)
ROUTER.register('dataversions', DataVersionViewSet)


urlpatterns = [
    path('docs/', include_docs_urls(title="RoR2Api documentation")),
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
]
