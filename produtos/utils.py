from produtos.models import Produto

def filtra_produtos(status_id, tipo_obra_id, artista_id):
    """
    Filtra os produtos com base nos parâmetros fornecidos (status, tipo de obra e artista).

    Parâmetros:
        status_id (int | None): ID do status do produto (pode ser None ou vazio para não filtrar).
        tipo_obra_id (int | None): ID do tipo de obra (pode ser None ou vazio para não filtrar).
        artista_id (int | None): ID do artista (pode ser None ou vazio para não filtrar).

    Retorna:
        QuerySet: Conjunto de produtos filtrado conforme os parâmetros fornecidos,
                  ordenado do mais recente para o mais antigo (ordem decrescente por ID).
    """
    produtos = Produto.objects.all().order_by('-id')

    if status_id:
        produtos = produtos.filter(status_id=status_id)
    if tipo_obra_id:
        produtos = produtos.filter(tipo_obra_id=tipo_obra_id)
    if artista_id:
        produtos = produtos.filter(artista_id=artista_id)

    return produtos