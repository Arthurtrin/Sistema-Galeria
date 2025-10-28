from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100, default='Nome não informado')
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos_artistas/', blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos_artistas/', blank=True, null=True)

    def __str__(self):
        return self.nome

class TipoObra(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Status(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    # Identificação
    codigo = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=100)
    tipo_obra = models.ForeignKey(TipoObra, on_delete=models.SET_NULL, null=True)
    artista = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    localizacao = models.CharField(max_length=100, null=True)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_produtos/', default='fotos_produtos/logo.png')

    def __str__(self):
        return self.nome
