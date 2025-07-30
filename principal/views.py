from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from usuarios.models import Perfil, Chave_Gerenciador
from produtos.models import Produto, Artista, TipoObra, Status

@login_required
def home(request):
    artistas = Artista.objects.all()
    tipos = TipoObra.objects.all()
    status = Status.objects.all()
    produtos = Produto.objects.all().order_by('-id')
    return render(request, 'principal/home.html', {
        "produtos": produtos,
        "tipos_obra": tipos,
        "artistas": artistas,
        "statuses": status})

@login_required
def filtro_produtos(request):
    status_id = request.GET.get('status', '')
    tipo_obra_id = request.GET.get('tipo_obra', '')
    artista_id = request.GET.get('artista', '')

    produtos = Produto.objects.all().order_by('-id')

    if status_id:
        produtos = produtos.filter(status_id=status_id)

    if tipo_obra_id:
        produtos = produtos.filter(tipo_obra_id=tipo_obra_id)

    if artista_id:
        produtos = produtos.filter(artista_id=artista_id)

    context = {
        'produtos': produtos,
        'tipos_obra': TipoObra.objects.all(),
        'artistas': Artista.objects.all(),
        'statuses': Status.objects.all(),
        'filtros': {
            'status': status_id,
            'tipo_obra': tipo_obra_id,
            'artista': artista_id,
        }
    }

    return render(request, 'principal/home.html', context)

@login_required
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})
