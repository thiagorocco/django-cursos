from django.contrib import admin
from core.models import Autor, Categoria, Compra, Editora, Livro

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Compra)