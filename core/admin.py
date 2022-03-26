# Register your models here.
from django.contrib import admin

from core.models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name_male', 'name_female']
    search_fields = ['name_male', 'name_female']


admin.site.register(Animal, AnimalAdmin)
