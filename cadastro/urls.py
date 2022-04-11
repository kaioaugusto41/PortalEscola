from django.urls import path
from . import views

urlpatterns = [
    #1 URL para página de cadastro de usuários
    path('', views.cadastro, name='cadastro'),

    #2 URL para página de cadastro de acessos
    path('/acessos', views.cadastro_acessos, name='cadastro_acessos'),

    path('/deletar', views.deletar_acessos, name='deletar_acessos'),

    path('/comunicados', views.cadastro_comunicados, name='cadastro_comunicados')

]