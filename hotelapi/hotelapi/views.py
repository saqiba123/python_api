from django.http import HttpResponse
def home_page(request):
    print("Django Rest Framwork is now live")
    return HttpResponse("Add Data here!")
