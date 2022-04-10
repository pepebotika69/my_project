from django.urls import path

from core.views import pet, asyncio

urlpatterns = [
    path('asyncio/', asyncio.index, name='basic_index'),
    path('pet/', pet.index, name='pet_index'),
]
