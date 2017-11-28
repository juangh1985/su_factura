from django.forms import *
from django import forms
from cliente.models import *


class formulario_cliente(ModelForm):
	class Meta:
		model = Cliente
		fields = ('cliente', 'correo', 'telefono','direccion', 'imagen', 'estado', 'empresa',)
		#~ widgets = {
		#~ 'tipo': Select(attrs={"class" :"select2",'placeholder': 'Tipo'}),
		#~ 'producto': Select(attrs={"class" :"select2",'placeholder': 'Producto'}),
		#~ 'cliente': Select(attrs={"class" :"select2",'placeholder': 'Cliente'}),
		#~ 'cantidad': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Cantidad'}),
		#~ 'importe': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Importe'}),
		#~ 'pcosto': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Precio de Costo'}),
		#~ }
