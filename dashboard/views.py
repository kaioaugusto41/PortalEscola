from django.shortcuts import render
from usuarios.models import Acessos
from .models import Comunicado
from django.conf import settings
from django.shortcuts import redirect

#1 PÁGINA INICIAL
def dash(request):

    #1 Validando se o usuário está autenticado
    if request.user.is_authenticated:

        #1.1 Capturando o usuário logado
        usuario = request.user

        #1.2 Capturando o usuário logado na base de acessos
        usuario = Acessos.objects.filter(email_usuario=usuario)

        #1.3 Caputurando todos os comunicados no banco de comunicados cadastrados por coordenadores
        comunicados = Comunicado.objects.all()

        #1.4 Dados que serão repassados para a página inicial
        dados = {

            # Tipo do usuário logado
            'tipo_usuario': usuario[0].tipo_usuario,

            # Lista com todos os comunicados cadastrados pelos coordenadores
            'comunicados': comunicados
        }

        #1.5 Validando se o usuário é do tipo Aluno
        if usuario[0].tipo_usuario == 'Aluno':

            #1.5.1 Redirecionando o usuário para o template de Alunos
            return render(request, 'dash_aluno/index_aluno.html', dados)
        
        #1.6 Validando se o usuário é do tipo Coordenador
        elif usuario[0].tipo_usuario == 'Coordenador':

            #1.6.1 Redirecionando o usuário para o template de Coordenadores
            return render(request, 'dash_coordenador/index_coordenador.html', dados)
    
    
    #2 Caso o usuário não esteja autenticado o mesmo será redirecionado para a página de Login
    else:
        return redirect('login')

