from django.shortcuts import render
from rest_framework import viewsets
from api.models import hotels
from api.serializers import hotelSerializer
# Create your views here.
class HotelsViewSet(viewsets.ModelViewSet):
    queryset= hotels.objects.all()
    serializer_class= hotelSerializer