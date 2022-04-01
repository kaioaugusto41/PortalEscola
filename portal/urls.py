from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('cadastro', include('cadastro.urls')),
    path('dashboard', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
