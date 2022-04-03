from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from usuarios.models import Acessos


# PÁGINA DE LOGIN 
def login(request):

    #1 Validando se o método do formulário de login é do tipo POST
    if request.method == "POST":

        #1.1 Capturando email fornecido no campo de email 
        email = request.POST.get('email', False)

        #1.2 Capturando senha fornecida no campo de senha 
        senha = request.POST.get('senha', False)

        #1.3 Validando se o usuário tem cadastro realizado
        if User.objects.filter(username=email).exists():

            #1.3.1 Capturando usuário cadastrado com base no email e senha fornecida
            user = auth.authenticate(request, username=email, password=senha)

            # 1.3.2 Validando se os dados estão corretos no banco e se sim redirecionando para a página inicial
            if user is not None:
                auth.login(request, user)
                usuario = Acessos.objects.filter(email_usuario=email)
                usuario = usuario[0].tipo_usuario
                return redirect('dash')

            # 1.3.3 Alertando ao usuário que os dados estão incorretos e redirecionando o mesmo para a página de login novamente
            else:
                messages.error(request, 'Verifique se os dados inseridos estão corretos!')
                redirect('login')
        
        #1.4 Caso o usuário informado não tenha sido encontrado no banco
        else:
            messages.error(request, 'Verifique se os dados inseridos estão corretos!')
            redirect('login')
    
    #2 Renderizando a página de login enquanto nenhuma ação tenha sido realizada
    return render(request, 'login.html')


# LOGOUT 
def logout(request):
    auth.logout(request)
    return redirect('login')
