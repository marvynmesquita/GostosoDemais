from django.db import models
import json

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    modo_preparo = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="receitas/")
    publicada = models.BooleanField(default=False)
    ingredientes = models.CharField(max_length=255, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    criador = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    def set_ingredientes(self, x):
        self.ingredientes = json.dumps(x)
    
    def get_ingredientes(self):
        return json.loads(self.ingredientes)
    