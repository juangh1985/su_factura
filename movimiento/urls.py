from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^movimiento_content', views.movimiento_content),
	url(r'^movimiento_form', views.movimiento_form),
	url(r'^movimiento_delete', views.movimiento_delete),
	url(r'^movimiento_edit', views.movimiento_edit),
	url(r'^movimiento_confirmar', views.movimiento_confirmar),
]

