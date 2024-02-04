from core.models import Categoria
from core.serializer import CategoriaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' #altera o campo procurado de pk(padrão) para o valor que você definir
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer