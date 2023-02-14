
from django.contrib import admin
from django.urls import path,include
from api.views import HotelsViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'hotels', HotelsViewSet)


urlpatterns = [
    path('', include(router.urls))
]
 