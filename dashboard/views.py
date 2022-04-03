from django.shortcuts import render
from usuarios.models import Acessos
from .models import Comunicado
from django.conf import settings
from django.shortcuts import redirect

def dash(request):
    if request.user.is_authenticated:
        usuario = request.user
        usuario = Acessos.objects.filter(email_usuario=usuario)
        comunicados = Comunicado.objects.all()
        dados = {
            'tipo_usuario': usuario[0].tipo_usuario,
            'comunicados': comunicados
        }
        if usuario[0].tipo_usuario == 'Aluno':
            return render(request, 'dash_aluno/index_aluno.html', dados)
        elif usuario[0].tipo_usuario == 'Coordenador':
            return render(request, 'dash_coordenador/index_coordenador.html', dados)
    else:
        return redirect('login')

def cadastro_acessos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        usuario = request.user
        usuario = Acessos.objects.filter(email_usuario=usuario)
        usuario = usuario[0].tipo_usuario
        if usuario == 'Coordenador':
            return render(request, 'dash_coordenador/pages/cadastros/acessos.html')
        else:
            return redirect('dash')