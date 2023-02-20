from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def student_create(request):
    # check it if the request method is post
    if request.method == 'POST':
        # save data into the json_data variable
        json_data = request.body
        # convert json data into stream (sequence of bits)
        stream = io.BytesIO(json_data)
        # convert stream of data into python-data
        py_data = JSONParser().parse(stream)
        # convert python data into complex data (model insta    nce/ query set)
        serializer = StudentSerializer(data=py_data)
        # validate data
        if serializer.is_valid():
            serializer.save()
            # send response msg in python
            #res = {'msg':'Data Created Successfully'}
            #return HttpResponse(data_json, content_type="application/json")
            return JsonResponse({'msg':'Data Created Successfully'})
