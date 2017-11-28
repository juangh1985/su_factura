from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^producto_content', views.producto_content),
	url(r'^producto_form', views.producto_form),
	url(r'^producto_delete', views.producto_delete),
	url(r'^producto_edit', views.producto_edit),

]

 



