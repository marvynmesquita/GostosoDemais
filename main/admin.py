from django.contrib import admin
from .models import Receitas, Categorias, Ingredientes
# Register your models here.
admin.site.register(Receitas)
admin.site.register(Categorias)
admin.site.register(Ingredientes)