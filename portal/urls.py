from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #1 URLs do app LOGIN
    path('', include('login.urls')),

    # URLs do app CADASTRO
    path('cadastro', include('cadastro.urls')),

    # URLs do app DASHBOARD
    path('dashboard', include('dashboard.urls')),

    # URLs do app ADMIN
    path('admin/', admin.site.urls),
]
