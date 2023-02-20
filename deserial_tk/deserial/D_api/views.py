from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializers import studentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
