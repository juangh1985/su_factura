from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^$', views.inicio),
	url(r'^empleado_content', views.empleado_content),
	url(r'^empleado_form', views.empleado_form),
	url(r'^empleado_delete', views.empleado_delete),
	url(r'^empleado_edit', views.empleado_edit),
]

