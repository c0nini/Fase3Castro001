from django import forms
from . models import Aroma, Producto

class AromaForm(forms.ModelForm):
    nombre = forms.CharField(label='Aroma', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción', max_length=2000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Aroma
        fields = ('nombre', 'descripcion',)

TIPO_PROD_CHOICES = [
        ('Tripack','Tripack'),
        ('Bótox','Bótox'),
        ('Spray Termoprotector','Spray Termoprotector'),
]


class ProductoForm(forms.ModelForm):
    tipo_producto = forms.ChoiceField(label='Tipo producto', choices=TIPO_PROD_CHOICES ,widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    aroma = forms.ModelChoiceField(queryset=Aroma.objects.all(),label='Aroma',widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    
    descripcion_prod = forms.CharField(label='Descripción', max_length=2000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    
    precio = forms.IntegerField(label='Precio', widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Producto
        fields = ('tipo_producto', 'aroma', 'descripcion_prod', 'precio')