from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length = 30)
    branch= models.CharField(max_length = 30)
    perc = models.FloatField()