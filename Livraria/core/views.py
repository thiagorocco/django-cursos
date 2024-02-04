from django.http import HttpResponse, JsonResponse

from django.views import View
from core.serializer import CategoriaSerializer


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
import json

class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' #altera o campo procurado de pk(padrão) para o valor que você definir
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
