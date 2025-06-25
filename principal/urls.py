from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/filtro', views.filtro_produtos, name='filtro_produtos')
]