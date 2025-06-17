from django.urls import path
from . import views

app_name = 'call'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('api/usuario-logado/', views.UsuarioLogadoView.as_view(), name='usuario-logado'),
]
