from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import Acessos, Aluno, Professor, Coordenador

def cadastro(request):
    if request.method == "POST":
        nome_completo = request.POST.get('nome_completo', False)
        email = request.POST.get('email', False)
        cpf = request.POST.get('cpf', False)
        senha = request.POST.get('senha', False)
        senha2 = request.POST.get('senha2', False)
        tipo_usuario = request.POST.get('tipo_usuario', False)

        #1 Valida se o usuário já é cadastrado na base de dados de acordo com o email
        if User.objects.filter(username=email).exists():
            print("Usuário já cadastrado!")
            redirect('cadastro')

        #2 Valida se o usuário já é cadastrado na base de dados de acordo com o email
        elif User.objects.filter(username = email).first():
            print("Usuário já cadastrado!")
            redirect('cadastro')

        #3 Valida se foi dada permissão na base de dados para o CPF fornecido
        elif Acessos.objects.filter(cpf_usuario=cpf).exists() == False:
            print("Usuário não encontrado!")
            redirect('cadastro')

        #4 Valida se as senhas fornecidas conferem
        elif senha != senha2:
            print("As senhas não conferem")
            redirect('cadastro')

        #5 Valida se o campo de Tipo Usuário não está em branco
        elif tipo_usuario == "Você é um...":
            print("O campo tipo de usuário não pode ficar em branco!")
            redirect('cadastro')

        #6 Caso passe em todas as validações, será validada a entrada por tipo de permissão (Aluno, Professor e Coordenador)
        else:

            #1 Validando a entrada de alunos
            if tipo_usuario == 'aluno':
                #1.1 Pegando do banco de dados de acessos o aluno com o cpf fornecido
                user = Acessos.objects.get(cpf_usuario=cpf)
                #1.2 Validando se o cpf fornecido possui permissão para se cadastrar como Aluno
                if user.tipo_usuario != 'Aluno':
                    print(user.tipo_usuario, )
                    print("Aluno não permitido para esse tipo de acesso!")
                    redirect('cadastro')
                #1.3 Validando se o cpf fornecido possui o e-mail cadastrado na base de dados de acessos
                elif str(user) != email:
                    print("Aluno não corresponde com a base de dados cadastrada!")
                    redirect('cadastro')
                #1.4 Se passado por todas as validações o aluno será cadastrado e redirecionado para a tela de login
                else:
                    #1.4.1 Criando e salvando usuário no banco de dados de usuários do django
                    user = User.objects.create_user(email=email, username=email, password=senha)
                    user.save()
                    #1.4.2 Criando e salvando dados do aluno em outra tabela de Aluno criada
                    aluno = Aluno.objects.create(nome_aluno=nome_completo, email_aluno=email, cpf_aluno=cpf, tipo_aluno=tipo_usuario)
                    aluno.save()
                    print("Aluno cadastrado com sucesso!")
                    print(nome_completo, cpf, senha, senha2, tipo_usuario)
                    return redirect('login')


            #2 validando a entrada de professores
            if tipo_usuario == 'professor':
                #2.1 Pegando do banco de dados de acessos o professor com o cpf fornecido
                user = Acessos.objects.get(cpf_usuario=cpf)
                #2.2 Validando se o cpf fornecido possui permissão para se cadastrar como Professor
                if user.tipo_usuario != 'Professor':
                    print(user.tipo_usuario)
                    print("Usuário não permitido para esse tipo de acesso!")
                    redirect('cadastro')
                #2.3 Validando se o cpf fornecido possui o e-mail cadastrado na base de dados de acessos
                elif str(user) != email:
                    print("Usuário não corresponde com a base de dados cadastrada!")
                    redirect('cadastro')
                #2.4 Se passado por todas as validações o professor será cadastrado e redirecionado para a tela de login
                else:
                    #2.4.1 Criando e salvando usuário no banco de dados de usuários do django
                    user = User.objects.create_user(email=email, username=email, password=senha)
                    user.save()
                    #2.4.2 Criando e salvando dados do professor em outra tabela de Aluno criada
                    professor = Professor.objects.create(nome_professor=nome_completo, email_professor=email, cpf_professor=cpf, tipo_professor=tipo_usuario)
                    professor.save()
                    print("Usuário cadastrado com sucesso!")
                    print(nome_completo, cpf, senha, senha2, tipo_usuario)
                    return redirect('login')


            #3 Validando a entrada de coordenadores
            if tipo_usuario == 'coordenador':
                user = Acessos.objects.get(cpf_usuario=cpf)
                if user.tipo_usuario != 'Coordenador':
                    print("Usuário não permitido para esse tipo de acesso!")
                    redirect('cadastro')
                elif str(user) != email:
                    print("Usuário não corresponde com a base de dados cadastrada!")
                    redirect('cadastro')
                else:
                    user = User.objects.create_user(email=email, username=email, password=senha)
                    user.save()
                    coordenador = Coordenador.objects.create(nome_coordenador=nome_completo, email_coordenador=email, cpf_coordenador=cpf, tipo_coordenador=tipo_usuario)
                    coordenador.save()
                    print("Usuário cadastrado com sucesso!")
                    print(nome_completo, cpf, senha, senha2, tipo_usuario)
                    return redirect('login')

    else:
        return render(request, 'cadastro.html')
        
    return render(request, 'cadastro.html')