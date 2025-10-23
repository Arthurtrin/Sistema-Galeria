from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('produtos/configuracao/', views.configuracao, name='configuracao'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/artistas_tipo-de-obra/', views.artista_tipoobra, name='artista_tipoobra'),
    path('produtos/tipo-de-obra/cadastrar/', views.cadastrar_tipoobra, name='cadastrar_tipoobra'),
    path('produtos/artista/cadastrar/', views.cadastrar_artista, name='cadastrar_artista'),
    path('produtos/tipo-de-obra/excluir/<int:tipo_id>', views.excluir_tipoobra, name='excluir_tipoobra'),
    path('produtos/artista/excluir/<int:artista_id>', views.excluir_artista, name='excluir_artista'),
    path('produtos/tipo-de-obra/editar/<int:tipo_id>', views.editar_tipoobra, name='editar_tipoobra'),
    path('produtos/artista/editar/<int:artista_id>', views.editar_artista, name='editar_artista'),
    path('produtos/status/editar/<int:status_id>', views.editar_status, name='editar_status'),
    path('produtos/status/excluir/<int:status_id>', views.excluir_status, name='excluir_status'),
    path('produtos/status/cadastrar/', views.cadastrar_status, name='cadastrar_status'),
    path('produtos/editar/', views.pg_editar_produto, name='pg_editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    
    
]