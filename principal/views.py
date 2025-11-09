from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto, Artista, TipoObra, Status
from .utils import *

@login_required
def home(request):
    """
    Exibe a página inicial do sistema.

    A função carrega informações sobre obras recentes, artistas recentes, bem como todos os artistas,
    além de identificar se o usuário atual é um gerenciador. 
    Também agrupa os artistas por ordem alfabetica para facilitar a navegação.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP.

    Retorna:
        HttpResponse: Página 'principal/home.html' renderizada com os dados de contexto.
    """

    # Renderiza a página inicial com os dados necessários
    return render(request, 'principal/home.html', {
        "artistas":Artista.objects.all().order_by('nome'), # Busca todos os artistas e ordena alfabeticamente
        'obras_recentes': Produto.objects.all().order_by('-id')[:8], # Busca as ultimas 8 obras cadastradas
        'artistas_recentes': Artista.objects.all().order_by('-id')[:8], # Busca os ultimos 8 artistas cadastrados
        'usuario_gerenciador': usuarioehgerenciador(request.user),  # Verifica se o usuário atual possui perfil de gerenciador
        })

@login_required
def detalhe_produto(request, produto_id):
    return render(request, 'produtos/detalhe_produto.html',{
        'produto': get_object_or_404(Produto, id=produto_id)})
