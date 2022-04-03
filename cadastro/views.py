from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from usuarios.models import Acessos, Aluno, Professor, Coordenador



# PÁGINA DE CADASTRO DE USUÁRIOS
def cadastro(request):

    if request.method == "POST":
        nome = request.POST.get('nome', False)
        sobrenome = request.POST.get('sobrenome', False)
        email = request.POST.get('email', False)
        cpf = request.POST.get('cpf', False)
        senha = request.POST.get('senha', False)
        senha2 = request.POST.get('senha2', False)
        tipo_usuario = request.POST.get('tipo_usuario', False)

        #1 Valida se o usuário já é cadastrado na base de dados de acordo com o email
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            redirect('cadastro')

        #2 Valida se o usuário já é cadastrado na base de dados de acordo com o email
        elif User.objects.filter(username = email).first():
            messages.error(request, 'Usuário já cadastrado!')
            redirect('cadastro')

        #3 Valida se foi dada permissão na base de dados para o email fornecido
        elif Acessos.objects.filter(email_usuario=email).exists() == False:
            messages.error(request, 'Usuário não encontrado no pré-cadastro!')
            redirect('cadastro')

        #4 Valida se as senhas fornecidas conferem
        elif senha != senha2:
            messages.error(request, 'As senhas não conferem!')
            redirect('cadastro')

        #5 Valida se o campo de Tipo Usuário não está em branco
        elif tipo_usuario == "Você é um...":
            messages.error('O de tipo usuário não pode ficar vazio!')
            redirect('cadastro')

        #6 Caso passe em todas as validações, será validada a entrada por tipo de permissão (Aluno, Professor e Coordenador)
        else:

            #1 Validando a entrada de alunos
            if tipo_usuario == 'aluno':

                #1.1 Pegando do banco de dados de acessos o aluno com o cpf fornecido
                user = Acessos.objects.get(email_usuario=email)

                #1.2 Validando se o email fornecido possui permissão para se cadastrar como Aluno
                if user.tipo_usuario != 'Aluno':
                    messages.error(request, 'Usuário não permititido para se cadastrar como aluno')
                    redirect('cadastro')

                #1.3 Validando se o email fornecido possui o cpf cadastrado na base de dados de acessos
                elif str(user) != cpf:
                    messages.error(request, 'O CPF informado não confere com o email pré-cadastrado!')
                    redirect('cadastro')

                #1.4 Se passado por todas as validações o aluno será cadastrado e redirecionado para a tela de login
                else:
                    #1.4.1 Criando e salvando usuário no banco de dados de usuários do django
                    user = User.objects.create_user(email=email, username=email, password=senha, first_name=nome, last_name=sobrenome)
                    user.save()

                    #1.4.2 Criando e salvando dados do aluno em outra tabela de Aluno criada
                    aluno = Aluno.objects.create(nome_aluno=nome+" "+sobrenome, email_aluno=email, cpf_aluno=cpf, tipo_aluno=tipo_usuario,)
                    aluno.save()
                    print("Aluno cadastrado com sucesso!")
                    messages.success(request, 'Cadastro realizado com sucesso!')
                    return redirect('login')


            #2 validando a entrada de professores
            if tipo_usuario == 'professor':

                #2.1 Pegando do banco de dados de acessos o professor com o email fornecido
                user = Acessos.objects.get(email_usuario=email)

                #2.2 Validando se o email fornecido possui permissão para se cadastrar como Professor
                if user.tipo_usuario != 'Professor':
                    messages.error(request, 'Usuário não permititido para se cadastrar como professor')
                    redirect('cadastro')

                #2.3 Validando se o email fornecido possui o cpf cadastrado na base de dados de acessos
                elif str(user) != cpf:
                    messages.error(request, 'O CPF informado não confere com o email pré-cadastrado!')
                    redirect('cadastro')

                #2.4 Se passado por todas as validações o professor será cadastrado e redirecionado para a tela de login
                else:

                    #2.4.1 Criando e salvando usuário no banco de dados de usuários do django
                    user = User.objects.create_user(email=email, username=email, password=senha, first_name=nome,last_name=sobrenome)
                    user.save()

                    #2.4.2 Criando e salvando dados do professor em outra tabela de Aluno criada
                    professor = Professor.objects.create(nome_professor=nome+" "+sobrenome, email_professor=email, cpf_professor=cpf, tipo_professor=tipo_usuario)
                    professor.save()
                    messages.success(request, 'Cadastro realizado com sucesso!')
                    return redirect('login')


            #3 Validando a entrada de coordenadores
            if tipo_usuario == 'coordenador':

                #3.1 Pegando do banco de dados de acessos o coordenador com o email fornecido
                user = Acessos.objects.get(email_usuario=email)

                #3.2 Validando se o email fornecido possui permissão para se cadastrar como Coordenador
                if user.tipo_usuario != 'Coordenador':
                    messages.error(request, 'Usuário não permititido para se cadastrar como coordenador')
                    redirect('cadastro')

                #3.3 Validando se o cpf fornecido possui o e-mail cadastrado na base de dados de acessos
                elif str(user) != cpf:
                    messages.error(request, 'O CPF informado não confere com o email pré-cadastrado!')
                    redirect('cadastro')

                #3.4 Se passado por todas as validações o coordenador será cadastrado e redirecionado para a tela de login
                else:

                    #3.4.1 Criando e salvando usuário no banco de dados de usuários do django
                    user = User.objects.create_user(email=email, username=email, password=senha, first_name=nome , last_name=sobrenome)
                    user.save()
                    
                    #3.4.2 Criando e salvando dados do coordenador em outra tabela de Aluno criada
                    coordenador = Coordenador.objects.create(nome_coordenador=nome+" "+sobrenome, email_coordenador=email, cpf_coordenador=cpf, tipo_coordenador=tipo_usuario)
                    coordenador.save()
                    messages.success(request, 'Cadastro realizado com sucesso!')
                    return redirect('login')

    else:
        return render(request, 'cadastro.html')
        
    return render(request, 'cadastro.html')


# PÁGINA DE CADASTRO DE ACESSOS
def cadastro_acessos(request):

    #1 Validando se o usuário está autenticado para cadastrar acessos
    if not request.user.is_authenticated:

        #1.1 Retornando o usuário para a página de login caso não esteja autenticado
        return redirect('login')
    
    #2 Caso o usuário esteja autenticado...
    else:

        #2.1 Capturando o usuário logado
        usuario = request.user

        #2.2 Capturando usuário logado na base de acessos
        usuario = Acessos.objects.filter(email_usuario=usuario)

        #2.3 Capturando o tipo de usuário do usuário logado
        usuario = usuario[0].tipo_usuario

        #2.4 Dados que serão passados para a página renderizada(acessos.html)
        dados = {

            #Tipo do usuário autenticado
            'tipo_usuario': usuario
        }

        #2.5 Se o usuário for do tipo Coordenador ele será redirecionado para a página de cadastro de acessos
        if usuario == 'Coordenador':
            return render(request, 'dash_coordenador/pages/cadastros/acessos.html', dados)

        #2.6 Caso o usuário não seja do tipo Coordenador ele será redirecionado para a página inicial
        else:
            return redirect('dash')