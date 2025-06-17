from django.shortcuts import render
from rest_framework import viewsets

from call.serializers import UsuarioSerializer
from usuario.models import Usuario


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
