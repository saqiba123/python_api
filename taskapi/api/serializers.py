from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40)