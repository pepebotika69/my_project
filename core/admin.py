from django.contrib import admin

from core.models import Animal, Pet


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name_male', 'name_female']
    search_fields = ['name_male', 'name_female']


admin.site.register(Animal, AnimalAdmin)


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'animal']
    search_fields = ['name', 'animal']


admin.site.register(Pet, PetAdmin)
