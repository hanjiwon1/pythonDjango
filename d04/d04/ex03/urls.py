from django.urls import path

from . import views

urlpatterns = [
	path('', views.tableIndex, name='tableIndex'),
]