from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.serializers import SerializerMethodField
from core.models import Categoria, Editora, Autor, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    editora = EditoraSerializer()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = '__all__'
        # Isso fará retornar o próximo campo da entidade após o ID
        depth = 1

    def get_autores(self, instance):
        nomes_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nomes_autores.append(autor.nome)
        return nomes_autores
