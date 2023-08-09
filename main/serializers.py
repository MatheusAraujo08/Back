from rest_framework import serializers
from .models import *

#vai converter o python dos models em json para a API
class PeopleSerializer(serializers.ModelSerializer):
    class Meta: 
        many = True
        model = People
        fields = '__all__'

class PlanetSerializer(serializers.ModelSerializer):
    class Meta: 
        many = True
        model = Planet
        fields = '__all__'

