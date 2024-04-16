from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/<int:id>', views.titulo),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
]
