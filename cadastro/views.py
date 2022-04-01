from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from alunos.models import Aluno

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('nome', False)
        email = request.POST.get('email', False)
        senha = request.POST.get('senha', False)
        senha2 = request.POST.get('senha2', False)
        ra = request.POST.get('r.a', False)
        tipo_usuario = request.POST.get('tipo_usuario', False)

        if Aluno.objects.filter(ra_aluno=ra).exists() == False:
            print("Usuário não encontrado!")
            redirect('cadastro')
        if senha != senha2:
            print("As senhas não conferem")
            redirect('cadastro')
        if tipo_usuario == "Você é um...":
            print("O campo tipo de usuário não pode ficar em branco!")
            redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print("Usuário já cadastrado!")
            redirect('cadastro')
        if User.objects.filter(username = usuario).first():
            print("Usuário já cadastrado!")
            redirect('cadastro')
        else:
            user = User.objects.create_user(username=usuario, email=email, password=senha)
            user.save()
            print("Usuário cadastrado com sucesso!")
            print(usuario, ra, senha, senha2, tipo_usuario)
            return redirect('login')
    else:
        return render(request, 'cadastro.html')
        
    return render(request, 'cadastro.html')