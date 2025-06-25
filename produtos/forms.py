from django import forms
from .models import Artista, TipoObra, Produto, Status

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if self.errors.get(field_name):
                css_class += ' is-invalid'
            field.widget.attrs['class'] = css_class

class ArtistaForm(BaseForm):
    class Meta:
        model = Artista
        fields = ['nome']

class TipoObraForm(BaseForm):
    class Meta:
        model = TipoObra
        fields = ['nome']

class StatusForm(BaseForm):
    class Meta:
        model = Status
        fields = ['nome']

class ProdutoForm(BaseForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
