from django.db import models


class Acessos(models.Model):
    nome_usuario = models.CharField(max_length=200)
    email_usuario = models.CharField(max_length=200)
    cpf_usuario = models.IntegerField(default=0, primary_key=True)
    opcoes = (
        ('Aluno','Aluno'),
        ('Professor','Professor'),
        ('Coordenador','Coordenador')
    )
    tipo_usuario = models.CharField(max_length=100, choices=opcoes)

    def __str__(self):
        return self.email_usuario


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    email_aluno = models.CharField(max_length=200)
    cpf_aluno = models.IntegerField(default=0, primary_key=True)
    tipo_aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno

class Professor(models.Model):
    nome_professor = models.CharField(max_length=200)
    email_professor = models.CharField(max_length=200)
    cpf_professor = models.IntegerField(default=0, primary_key=True)
    tipo_professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_professor

class Coordenador(models.Model):
    nome_coordenador = models.CharField(max_length=200)
    email_coordenador = models.CharField(max_length=200)
    cpf_coordenador = models.IntegerField(default=0, primary_key=True)
    tipo_coordenador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_coordenador