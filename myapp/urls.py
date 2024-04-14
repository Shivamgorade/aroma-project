# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
path('order/', views.order_form, name='order_form'),

]
