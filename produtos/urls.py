from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
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
    path('produtos/filtos/artistas/', views.filtros_artistas, name='filtros_artistas'),
    path('produtos/filtos/obras/', views.filtros_obras, name='filtros_obras'),
    path('produtos/filtos/status/', views.filtros_status, name='filtros_status'),
    
    
]