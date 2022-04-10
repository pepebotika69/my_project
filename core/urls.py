from django.urls import path

from core.views import pet, asyncio

urlpatterns = [
    path('asyncio/', asyncio.index, name='basic_index'),
    # pet
    path('pet/', pet.index, name='pet_index'),
    path('pet/all', pet.get_all_pets, name='pet_all'),
]
