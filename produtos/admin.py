from django.contrib import admin
from .models import Produto, Artista, TipoObra, Status

# Register your models here.
admin.site.register(Produto)
admin.site.register(Artista)
admin.site.register(TipoObra)
admin.site.register(Status)
