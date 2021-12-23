from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField()
    sal = models.IntegerField()

    def __str__(self):
        return self.name
    
class DF(models.Model):
    emp = OneToOneField(Emp, on_delete=models.CASCADE,)
    dname = models.CharField(max_length=30, primary_key=True)
    
    
    def __str__(self):
        return self.dname    

