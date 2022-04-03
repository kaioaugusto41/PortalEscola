from django.urls import path
from . import views

urlpatterns = [
    #1 URL para página de cadastro de usuários
    path('', views.cadastro, name='cadastro'),

    #2 URL para página de cadastro de acessos
    path('/acessos', views.cadastro_acessos, name='cadastro_acessos')
]