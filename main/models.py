from django.db import models
import json
from django.core import serializers

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingredientes(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    modo_preparo = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    ingredientes = models.CharField(max_length=1000, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    def set_ingredientes(self, quantidade, ingredientes):
        self.ingredientes = serializers.serialize("json", quantidade, ingredientes)
    
    def get_ingredientes(self):
        return json.loads(self.ingredientes)
    