from django.views.generic import TemplateView
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from call.models import Chamada
from call.serializers import (
    ChamadaUsuarioSerializer,
    ChamadaTecnicoSerializer,
    UsuarioSerializer,
)
from usuario.models import Usuario

class ChamadaUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChamadaUsuarioSerializer

    def get_queryset(self):
        return Chamada.objects.filter(usuario=self.request.user.usuario, status_chamado='1')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user.usuario, status_chamado='1')


# View para técnico
class ChamadaTecnicoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChamadaTecnicoSerializer

    def get_queryset(self):
        if not self.request.user.usuario.is_tecnico:
            raise serializers.ValidationError("Apenas técnicos podem acessar esta rota.")
        return Chamada.objects.filter(status_chamado='1')

    def perform_create(self, serializer):
        raise serializers.ValidationError("Técnico não pode criar chamados.")

    def perform_update(self, serializer):
        serializer.save()


# Retorna dados do usuário logado
class UsuarioLogadoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user.usuario)
        return Response(serializer.data)


class ChamadosFinalizadosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChamadaTecnicoSerializer

    def get_queryset(self):
        if not self.request.user.usuario.is_tecnico:
            raise serializers.ValidationError("Apenas técnicos podem acessar esta rota.")
        return Chamada.objects.filter(status_chamado__in=['2', '3']).order_by('-data')


class ChamadosUsuarioFinalizadosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChamadaTecnicoSerializer  # Ou ChamadaUsuarioSerializer se quiser sem dados do usuário

    def get_queryset(self):
        return Chamada.objects.filter(
            usuario=self.request.user.usuario,
            status_chamado__in=['2', '3']
        ).order_by('-data')



class Index(TemplateView):
    template_name = 'call/index.html'


