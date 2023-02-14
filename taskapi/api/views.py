from django.shortcuts import render
from .models import Student
from.serializers import studentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create student data model instance.
def student_data(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = studentSerializer(stu)
    #just converted model data into python obj
    #now convert python obj to json
    #json_data= JSONRenderer().render(serializer.data)
    #send response to client
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Create query set pf all student data
def student_list(request):
    stu = Student.objects.all()
    serializer = studentSerializer(stu, many=True)
    #just converted model data into python obj
    #now convert python obj to json
    json_data= JSONRenderer().render(serializer.data)
    #send response to client
    return HttpResponse(json_data, content_type='application/json')
