from django import forms
from .models import Producto, Cliente, Venta, Categoria, TipoPersona, TipoVenta

BS4_FORM_DICT = {"class":"form-control"}


class ProductoForm(forms.ModelForm):
    object_list = Categoria.objects.all()
    category = forms.ModelChoiceField(label="Categorías:",queryset=object_list, widget=forms.Select(attrs=BS4_FORM_DICT))
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=BS4_FORM_DICT),
            'price': forms.NumberInput(attrs=BS4_FORM_DICT),
            'iva': forms.Select(choices=[("0","Excento"),("12","12%"),("10","10%"),("9","9%")],attrs=BS4_FORM_DICT),
            'total': forms.NumberInput(attrs={"hidden":""}),
            
        }
        labels = {
            'name': 'Nombre del Producto:',
            'price': 'Precio unitario:',
            'total': '',
        }


class ClienteForm(forms.ModelForm):
    object_list = TipoPersona.objects.all()
    
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=BS4_FORM_DICT),
            'last_name': forms.TextInput(attrs=BS4_FORM_DICT),
            'cedula': forms.NumberInput(attrs=BS4_FORM_DICT),
            'tipo_persona': forms.Select(attrs=BS4_FORM_DICT)
        }
        labels = {
            'name': 'Nombres:',
            'cedula': 'Cedula o Rif:',
            'last_name': 'Apellidos:',
        }


class VentaForm(forms.ModelForm):
    object_list = TipoVenta.objects.all()
    object_list_2 = Cliente.objects.all()
    object_list_3 = Producto.objects.all()
    
    cliente = forms.ModelChoiceField(label="Cliente a Facturar:",queryset=object_list_2, widget=forms.Select(attrs=BS4_FORM_DICT))
    tipo_venta = forms.ModelChoiceField(label="Tipo de Venta:",queryset=object_list, widget=forms.Select(attrs=BS4_FORM_DICT))
    productos = forms.ModelMultipleChoiceField(label="",queryset=object_list_3, widget=forms.SelectMultiple(attrs={"hidden":""}))
    
    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            'total':forms.NumberInput(attrs=BS4_FORM_DICT),
        }
        labels = {
            'name': 'Nombres:',
            'cedula': 'Cedula o Rif:',
            'last_name': 'Apellidos:',
        }


class CategoryForm(forms.ModelForm):
    object_list = Categoria.objects.all().order_by("father__name")
    father = forms.ModelChoiceField(label="Categoría Pater:", queryset=object_list,required=False, widget=forms.Select(attrs=BS4_FORM_DICT))
    class Meta:
        model = Categoria
        fields = "__all__"
        widgets={
            'name': forms.TextInput(attrs=BS4_FORM_DICT),
        }
        labels={
            'name': 'Nombre de la Categoría:',
        }