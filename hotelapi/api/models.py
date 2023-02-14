from django.db import models

# Create your models here.

#for hotels

class hotels(models.Model):
    Property =models.CharField(max_length=40)
    Rating = models.CharField(max_length=40)
    Destination = models.CharField(max_length=40)
    Country = models.CharField(max_length=40) 

