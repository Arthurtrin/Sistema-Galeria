from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil, Chave_Gerenciador
from .forms import ProdutoForm, ArtistaForm, TipoObraForm, StatusForm
from .models import Produto, Artista, TipoObra, Status
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def configuracao(request):
    usuario = request.user
    try:
        perfil = Perfil.objects.get(usuario=usuario)
    except Perfil.DoesNotExist:
        mensagem = 'Perfil não encontrado'
        return render(request, 'principal/erro.html', {'mensagem': mensagem})

    if perfil.tipo not in ['gerenciador', 'supervisor']:
        mensagem = 'Você não tem permissão para acessar esta página.'
        return render(request, 'principal/erro.html', {'mensagem': mensagem})
    return render(request, 'produtos/configuracao.html')

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

def editar_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')
    else:
        return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')

def excluir_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')

def cadastrar_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos:artista_tipoobra') + '?aba=status')
    else:
        return redirect('produtos:artista_tipoobra')

