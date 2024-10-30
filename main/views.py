from django.shortcuts import render
from django.http import HttpResponse
from main.models import Receitas, Categorias
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.core import serializers


class Homepage(View):
    def get(self, request):
        receitas = Receitas.objects.all()
        receitas_list = serializers.serialize("json", list(receitas))
        context = {"receitas": receitas_list}
        return render(request, "main/index.html", context)

class ReceitaView(DetailView):
    model = Receitas
    template_name = "main/receita.html"
    context_object_name = "receita"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredientes"] = serializers.serialize("json", list(Ingredientes.objects.all()))
        return context

class ReceitasCreateView(CreateView):
    model = Receitas
    fields = "__all__"
    sucess_url = reverse_lazy("receitas")
