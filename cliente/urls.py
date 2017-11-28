from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^cliente_content', views.cliente_content),
	url(r'^cliente_form', views.cliente_form),
	url(r'^cliente_delete', views.cliente_delete),
	url(r'^cliente_edit', views.cliente_edit),
]

