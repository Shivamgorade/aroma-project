# myapp/urls.py

from django.urls import path
from . import views
from .views import order_view

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('order/', order_view, name='order_page'),


]
