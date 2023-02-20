from rest_framework import serializers
from .models import students


class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    school = serializers.CharField(max_length=50)

    #after reading the data from db now we can use create method to add data in db
    def create(self, validated_data):
        return students.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.school = validated_data.get('school', instance.school)
        instance.save()
        return instance