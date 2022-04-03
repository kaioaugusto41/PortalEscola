from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from usuarios.models import Acessos

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        senha = request.POST.get('senha', False)
        if User.objects.filter(username=email).exists():
            user = auth.authenticate(request, username=email, password=senha)
            if user is not None:
                auth.login(request, user)
                print("Login efetuado com sucesso!")
                print(email, senha)
                return redirect('dash_aluno')
                
            else:
                messages.error(request, 'Verifique se os dados inseridos estão corretos!')
                redirect('login')
        
        else:
            messages.error(request, 'Verifique se os dados inseridos estão corretos!')
            redirect('login')
    
    return render(request, 'login.html')