from accounts.views.sigin import Sigin
from django.urls import path

urlpatterns = [
    path('signin', Sigin.as_view())    
]