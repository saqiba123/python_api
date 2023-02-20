from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.
from .models import students
from .serializers import studentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# class student_update(request):
def studentapi(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = students.objects.get(id=id)
            serializer = studentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = students.objects.all()
        serializer = studentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = students.objects.get(id=id)
        # for partial update use partial= TRUE
        serializer = studentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data is updated!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = students.objects.get(id=id)
        stu.delete()
        res = {"msg": "Data is deleted!"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonRenponse(res, safe=False)
