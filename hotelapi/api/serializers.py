from rest_framework import serializers
from api.models import hotels

#hotel serializers

class hotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=hotels
        fields="__all__"
