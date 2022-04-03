from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_aluno, name='dash_aluno')
]
