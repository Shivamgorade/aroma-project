# urls.py
from django.urls import path
from .views import menu, place_order

urlpatterns = [
    path('', menu, name='menu'),
]
