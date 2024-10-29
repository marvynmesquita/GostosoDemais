from django.db import models


# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Ingredientes(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=50)
    receita = models.ForeignKey(Receitas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    modo_preparo = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="receitas/")
    publicada = models.BooleanField(default=False)
    ingredientes = models.ManyToManyField(Ingredientes)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tags")
    criador = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Usuarios(models.Model):
    usuario = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="usuarios/")
    receitas = models.ManyToManyField(Receitas)
    favoritas = models.ManyToManyField(Receitas, related_name="favoritas")
    seguidos = models.ManyToManyField(
        "self", related_name="seguidores", symmetrical=False
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.username


class Tags(models.Model):
    nome = models.CharField(max_length=50)
    receitas = models.ManyToManyField(Receitas)

    def __str__(self):
        return self.nome
