from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Receitas, Categorias
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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
    context = {"receita": Receitas.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReceitasCreateView(CreateView):
    model = Receitas
    fields = [
        "nome",
        "modo_preparo",
        "ingredientes",
        "publicada",
        "categoria",
    ]
    template_name = "main/receita_form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)


class ReceitasUpdateView(UpdateView):
    model = Receitas
    fields = [
        "nome",
        "modo_preparo",
        "ingredientes",
        "publicada",
        "categoria",
    ]
    template_name = "main/receita_form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)


class ReceitasDeleteView(DeleteView):
    model = Receitas
    template_name = "main/receita_delete.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
