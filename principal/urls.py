from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/detalhe/<int:produto_id>', views.detalhe_produto, name='detalhe_produto'),
]