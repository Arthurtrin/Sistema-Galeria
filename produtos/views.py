from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil
from .forms import ProdutoForm, ArtistaForm, TipoObraForm, StatusForm
from .models import Produto, Artista, TipoObra, Status
from django.http import HttpResponseRedirect
from django.urls import reverse
from itertools import groupby
from .utils import *
from principal.utils import *

def ver_artista(request, id):
    """
    Exibe a página de detalhes de um artista específico.

    A função busca o artista pelo ID informado e carrega todas as obras (produtos)
    associadas a ele. Também envia a lista completa de artistas para permitir
    navegação entre perfis.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP.
        id (int): ID do artista a ser exibido.

    Retorna:
        HttpResponse: Página 'produtos/mostra_artista.html' renderizada com:
            - o artista selecionado,
            - todas as suas obras (produtos),
            - e a lista completa de artistas cadastrados.
    """
    # Busca o artista pelo ID; retorna erro 404 se não for encontrado
    artista = get_object_or_404(Artista, id=id)

    # Renderiza o template com os dados do artista e suas obras
    return render(request, 'produtos/mostra_artista.html', {
        'artista': artista,                                      # Artista atual
        'artistas': Artista.objects.all().order_by('nome'),      # Lista completa de artistas
        'obras': Produto.objects.filter(artista=artista)         # Obras associadas ao artista
    })

def todosartistas(request):
    """
    Exibe a página com todos os artistas cadastrados no sistema.

    A função obtém todos os artistas do banco de dados e os agrupa
    pela primeira letra do nome, para facilitar a navegação no template.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP.

    Retorna:
        HttpResponse: Página 'produtos/todos_artistas.html' renderizada com:
            - a lista completa de artistas,
            - e os grupos de artistas organizados por letra inicial.
    """
    # Busca todos os artistas cadastrados
    artistas = Artista.objects.all()

    # Cria um dicionário onde as chaves são letras e os valores são listas de artistas
    grupos = {}
    for letra, grupo in groupby(artistas, key=lambda a: a.nome[0].upper()):
        grupos[letra] = list(grupo)

    # Renderiza o template com os artistas e seus respectivos grupos
    return render(request, 'produtos/todos_artistas.html', {
        "artistas": artistas,  # Lista completa de artistas
        'grupos': grupos       # Artistas agrupados pela letra inicial do nome
    })
    
def todasobras(request):
    """
    Exibe a página com todas as obras (produtos) cadastradas no sistema.

    A função carrega todas as obras, bem como os artistas, tipos de obra e status,
    para permitir navegação, filtragem e exibição completa no template.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP.

    Retorna:
        HttpResponse: Página 'produtos/todas_obras.html' renderizada com:
            - todas as obras cadastradas (ordenadas do mais recente ao mais antigo),
            - a lista completa de artistas,
            - a lista de tipos de obra,
            - e a lista de status disponíveis.
    """
    # Renderiza o template com todos os dados necessários
    return render(request, 'produtos/todas_obras.html', {
        'artistas': Artista.objects.all(),             # Lista completa de artistas
        'tipos': TipoObra.objects.all(),               # Lista de tipos de obra
        'status': Status.objects.all(),                # Lista de status disponíveis
        'obras': Produto.objects.all().order_by('-id'),# Todas as obras (do mais novo ao mais antigo)
    })

@login_required
def filtro_produtos(request):
    """
    Filtra e exibe as obras de acordo com os parâmetros enviados via requisição GET.

    A função permite ao usuário refinar a listagem de obras conforme três critérios opcionais:
    - status da obra,
    - tipo de obra,
    - artista responsável.

    Se um ou mais filtros não forem informados, o sistema exibirá todos os registros
    correspondentes aos filtros aplicados. O resultado é mostrado na página de listagem geral
    de obras.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP contendo os parâmetros de filtro
        ('status', 'tipo_obra' e 'artista').

    Retorna:
        HttpResponse: Página 'produtos/todas_obras.html' renderizada com:
            - as obras filtradas,
            - as listas completas de artistas, tipos de obra e status disponíveis.
    """

    # Obtém os valores dos filtros passados pela URL (ou vazios, se não existirem)
    status_id = request.GET.get('status', '')
    tipo_obra_id = request.GET.get('tipo_obra', '')
    artista_id = request.GET.get('artista', '')

    # Monta o contexto com os produtos filtrados e as listas auxiliares
    context = {
        'obras': filtra_produtos(status_id, tipo_obra_id, artista_id),  # Resultado da filtragem
        'tipos': TipoObra.objects.all(),                                # Lista de tipos de obra
        'artistas': Artista.objects.all(),                              # Lista de artistas
        'status': Status.objects.all(),                                 # Lista de status
    }

    # Renderiza o template com os resultados
    return render(request, 'produtos/todas_obras.html', context)

@login_required
def configuracao(request):
    try:
        perfil = Perfil.objects.get(usuario=request.user)
    except Perfil.DoesNotExist:
        mensagem = 'Perfil não encontrado'
        return render(request, 'principal/erro.html', {'mensagem': mensagem})

    if perfil.tipo not in ['gerenciador', 'supervisor']:
        mensagem = 'Você não tem permissão para acessar esta página.'
        return render(request, 'principal/erro.html', {'mensagem': mensagem})
    return render(request, 'produtos/configuracao.html', {
        'usuario_gerenciador': usuarioehgerenciador(request.user),  # Verifica se o usuário atual possui perfil de gerenciador
        })


def cadastrar_artistas(request):
    return render(request, 'produtos/artistas.html')

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})

@login_required
def artista_tipoobra(request):
    usuario = request.user
    perfil = Perfil.objects.get(usuario=usuario)

    # Recuperar o valor da aba ativa da URL, ou usar 'tipos' como padrão
    aba = request.GET.get('aba', 'tipos')

    artista = Artista.objects.all()
    tipo_obra = TipoObra.objects.all()
    status = Status.objects.all()

    return render(request, 'produtos/artista_tipoobra.html', {
        "artistas": artista,
        "tipos_obra": tipo_obra,
        "status_list": status,
        "aba": aba  # <<< esta linha é essencial
    })

@login_required
def cadastrar_tipoobra(request):
    if request.method == 'POST':
        form = TipoObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:artista_tipoobra')
    else:
        return redirect('produtos:artista_tipoobra')

@login_required
def excluir_tipoobra(request, tipo_id):
    tipo = get_object_or_404(TipoObra, id=tipo_id)
    tipo.delete()
    return redirect ('produtos:artista_tipoobra')

@login_required
def cadastrar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=artistas')
    else:
        return redirect('produtos:artista_tipoobra')

@login_required
def excluir_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    artista.delete()
    return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=artistas')

@login_required
def editar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=artistas')
    else:
        return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=artistas')

@login_required
def editar_tipoobra(request, tipo_id):
    tipo = get_object_or_404(TipoObra, id=tipo_id)
    if request.method == 'POST':
        form = TipoObraForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('produtos:artista_tipoobra')
    else:
        return redirect('produtos:artista_tipoobra')

@login_required
def editar_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')
    else:
        return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')

@login_required
def excluir_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')

@login_required
def cadastrar_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')
    else:
        return redirect('produtos:artista_tipoobra')

@login_required
def pg_editar_produto(request):
    produtos = Produto.objects.all().order_by('-id')
    return render(request, 'produtos/pag_edt_produtos.html', {"produtos":produtos})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produtos:pg_editar_produto')

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:pg_editar_produto')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})