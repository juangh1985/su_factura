from django.forms import *
from django import forms
from asistencia.models import *


class formulario_asistencia(ModelForm):
	class Meta:
		model = calendario
		fields = ['trabajador', 'inicio']
		widgets = {
		'trabajador': Select(attrs={"class" :"select2",'placeholder': 'trabajador'}),
		'inicio': TextInput(attrs={'id' :'datepicker','class' :'form-control','placeholder': 'inicio'}),
		#~ 'fin': TextInput(attrs={'id' :'datepicker1','class' :'form-control','placeholder': 'Cantidad'}),
}

