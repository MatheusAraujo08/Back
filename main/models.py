from django.db import models
from django.utils import timezone 

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=100) #varchar
    clima = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now()) #datetime
    diameter = models.DecimalField(max_digits=10, decimal_places=2)
    gravity = models.IntegerField() #int
    population = models.BigIntegerField() #bigint

    def __str__(self):
        return self.name 
    

#tabela!!
class People(models.Model):
    name = models.CharField(max_length=100) #varchar
    birth = models.CharField(max_length=50) #varchar
    eye = models.CharField(max_length=50) #varchar
    gander = models.CharField(max_length=50, blank=False, null=True) #varchar 
    hair = models.CharField(max_length=50, blank=False) #varchar
    height = models.DecimalField(max_digits=10, decimal_places=2) #decimal, float
    mass = models.DecimalField(max_digits=10, decimal_places=2) #decimal, float
    created = models.DateTimeField(default=timezone.now()) #datetime
    planet = models.ForeignKey(Planet, related_name="planet", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 


