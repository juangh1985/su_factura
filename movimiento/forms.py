from django.forms import *
from django import forms
from movimiento.models import *


class formulario_movimiento(ModelForm):
	class Meta:
		model = movimiento
		fields = ['tipo', 'producto', 'cliente','cantidad', 'importe', 'pcosto']
		widgets = {
		'tipo': Select(attrs={"class" :"select2",'placeholder': 'Tipo'}),
		'producto': Select(attrs={"class" :"select2",'placeholder': 'Producto'}),
		'cliente': Select(attrs={"class" :"select2",'placeholder': 'Cliente'}),
		'cantidad': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Cantidad'}),
		'importe': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Importe'}),
		'pcosto': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Precio de Costo'}),
		}
