from django.contrib import admin
from .models import * #iportado todos os models

# Register your models here.

class detPlanet(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Planet, detPlanet) #aplica as configs

class detPeople(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(People, detPeople) #aplica as configs

