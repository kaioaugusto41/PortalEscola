from django.urls import path
from . import views

urlpatterns = [
    #1 URL para a página de Login
    path('', views.login, name='login'),

    #2 URL para realizar o Logout
    path('logout', views.logout, name='logout')
]