from django.db import models

# Create your models here.
class Employee (models.Model):
    id= models.IntegerField
    name = models.CharField(max_length = 50)