from django.db import models

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    ra_aluno = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_aluno
