from django.contrib import admin
from .models import Acessos, Aluno, Professor, Coordenador

admin.site.register(Acessos)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)