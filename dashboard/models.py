from django.db import models
from usuarios.models import Coordenador

class Comunicado(models.Model):
    titulo_comunicado = models.CharField(max_length=300)
    descricao_comunicado = models.TextField(max_length=300)
    texto_comunicado = models.TextField()
    data_comunicado = models.DateField()
    
    def __str__(self):
        return self.titulo_comunicado

