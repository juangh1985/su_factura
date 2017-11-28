from django.forms import *
from django import forms
from empleado.models import *


class formulario_empleado(ModelForm):
	class Meta:
		model = Trabajador
		fields = ['nombre', 'imagen', 'direccion','carne','correo', 'titulo', 'graduado', 'telefono', 'cargo', 'estado']
		#~ widgets = {
		#~ 'tipo': Select(attrs={"class" :"select2",'placeholder': 'Tipo'}),
		#~ 'producto': Select(attrs={"class" :"select2",'placeholder': 'Producto'}),
		#~ 'empleado': Select(attrs={"class" :"select2",'placeholder': 'empleado'}),
		#~ 'cantidad': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Cantidad'}),
		#~ 'importe': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Importe'}),
		#~ 'pcosto': TextInput(attrs={'type' :'number','class' :'form-control','placeholder': 'Precio de Costo'}),
		#~ }


