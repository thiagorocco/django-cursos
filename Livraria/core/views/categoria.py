from core.serializer import CategoriaSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Categoria


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
