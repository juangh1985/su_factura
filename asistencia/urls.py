from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^asistencia_content', views.asistencia_content),
	url(r'^asistencia_form', views.asistencia_form),
]

