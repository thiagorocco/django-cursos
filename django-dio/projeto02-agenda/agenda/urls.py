from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/<int:id>', views.titulo),
    path('agenda/', views.lista_eventos)
]
