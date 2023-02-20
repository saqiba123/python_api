from django.urls import path
from deserialapi import views

urlpatterns = [
    path('stucreate/',views.student_create),
]
