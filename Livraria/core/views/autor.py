from rest_framework.viewsets import ModelViewSet
from core.models import Autor
from core.serializer import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
