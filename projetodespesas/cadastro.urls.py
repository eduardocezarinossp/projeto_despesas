from django.urls import path
from .import views
urlpatterns = [
    path('', views.ola_mundo, name ='ola_mundo'),
    path('segundapagina', views.segundapagina, name ='segundapagina'),
]