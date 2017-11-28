from django.forms import *
from django import forms
from producto.models import *


class formulario_producto(ModelForm):
	class Meta:
		model = producto
		fields = ['imagen', 'nombre', 'tipo','pcosto', 'pventa', 'fecha', 'observacion', 'activo']
