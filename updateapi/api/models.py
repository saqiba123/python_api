from django.db import models

# Create your models here.
# create database

class students(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    school = models.CharField(max_length=50)

    


