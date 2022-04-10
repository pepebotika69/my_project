from django.urls import path

from core.views import basic
from core.views import asyncio

urlpatterns = [
    path('basic/', basic.index, name='basic_index'),
    path('asyncio/', asyncio.index, name='basic_index'),
]
