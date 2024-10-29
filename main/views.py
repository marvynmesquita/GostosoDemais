from django.shortcuts import render
from django.http import HttpResponse
from .models import Categorias, Ingredientes, Receitas, Usuarios, Tags


def index(request):
    return HttpResponse("Hello, World!")


def receitas(request):
    receitas = Receitas.objects.all()
    return render(request, "receitas.html", {"receitas": receitas})


def receita_detail(request, receita_id):
    receita = Receitas.objects.get(pk=receita_id)
    return render(request, "receita_detail.html", {"receita": receita})


def categorias(request):
    categorias = Categorias.objects.all()
    return render(request, "categorias.html", {"categorias": categorias})


def categoria_detail(request, categoria_id):
    categoria = Categorias.objects.get(pk=categoria_id)
    return render(request, "categoria_detail.html", {"categoria": categoria})


def ingredientes(request):
    ingredientes = Ingredientes.objects.all()
    return render(request, "ingredientes.html", {"ingredientes": ingredientes})


def ingrediente_detail(request, ingrediente_id):
    ingrediente = Ingredientes.objects.get(pk=ingrediente_id)
    return render(request, "ingrediente_detail.html", {"ingrediente": ingrediente})


def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, "usuarios.html", {"usuarios": usuarios})


def usuario_detail(request, usuario_id):
    usuario = Usuarios.objects.get(pk=usuario_id)
    return render(request, "usuario_detail.html", {"usuario": usuario})


def tags(request):
    tags = Tags.objects.all()
    return render(request, "tags.html", {"tags": tags})


def tag_detail(request, tag_id):
    tag = Tags.objects.get(pk=tag_id)
    return render(request, "tag_detail.html", {"tag": tag})


def buscar(request):
    query = request.GET.get("query")
    receitas = Receitas.objects.filter(nome__icontains=query)
    return render(request, "buscar.html", {"receitas": receitas})


# Create your views here.
