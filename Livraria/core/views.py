from django.http import HttpResponse
from django.views import View
from core.models import Categoria

import json

def teste(request):
    return HttpResponse('Olá, mundo do Django')

def teste2(request):
    return HttpResponse('Página 2')

class CategoriaView(View):
    def get(self, request):
        data = list(Categoria.objects.values())
        formated_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formated_data, content_type="application/json")