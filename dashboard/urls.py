from urllib import request
from django.urls import path
from . import views

#1 URL da página inicial
urlpatterns = [
    path('', views.dash, name='dash'),
]
