from django.db import models


#1 TABELA DE ACESSOS (COORDENADORES PODEM CADASTRARS)
class Acessos(models.Model):
    nome_usuario = models.CharField(max_length=200)
    email_usuario = models.CharField(max_length=200, primary_key=True)
    cpf_usuario = models.IntegerField(default=0)
    opcoes = (
        ('Aluno','Aluno'),
        ('Professor','Professor'),
        ('Coordenador','Coordenador')
    )
    tipo_usuario = models.CharField(max_length=100, choices=opcoes)

    def __str__(self):
        return str(self.cpf_usuario)

#2 TABELA DE ALUNOS (COORDENADORES E PROFESSORES PODEM CADASTRAR)
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    email_aluno = models.CharField(max_length=200, primary_key=True)
    cpf_aluno = models.IntegerField(default=0)
    tipo_aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno

#3 TABELA DE PROFESSORES (COORDENADORES PODEM CADASTRAR)
class Professor(models.Model):
    nome_professor = models.CharField(max_length=200)
    email_professor = models.CharField(max_length=200, primary_key=True)
    cpf_professor = models.IntegerField(default=0)
    tipo_professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_professor

#4 TABELA DE COORDENADORES (COORDENADORES PODEM CADASTRAR)
class Coordenador(models.Model):
    nome_coordenador = models.CharField(max_length=200)
    email_coordenador = models.CharField(max_length=200, primary_key=True)
    cpf_coordenador = models.IntegerField(default=0)
    tipo_coordenador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_coordenador