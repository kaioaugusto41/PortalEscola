from urllib import request
from django.urls import path
from . import views
import secrets


def gerar_url():
    return secrets.token_hex(6)

urlpatterns = [
    path('', views.dash, name='dash'),
    path('/cadastro_acessos', views.cadastro_acessos, name='cadastro_acessos')
]
