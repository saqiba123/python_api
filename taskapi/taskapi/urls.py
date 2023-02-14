from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("Studentinfo/<int:pk>",views.student_data),
    path("Studentinfo/",views.student_list),
]
