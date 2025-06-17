from rest_framework import serializers
from .models import Chamada
from usuario.models import Usuario
from django.contrib.auth.models import User

# Serializador embutido para exibir informações do User (opcional)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializador para o modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'nome', 'escola', 'inep', 'is_tecnico']

# Serializador para usuários comuns
class ChamadaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamada
        fields = ['id', 'manutencao', 'descricao', 'data', 'data_up', 'status_chamado']
        read_only_fields = ['data', 'data_up']

# Serializador para técnicos – somente o status é editável, o restante é leitura
class ChamadaTecnicoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)  # Aninhado

    class Meta:
        model = Chamada
        fields = ['id', 'manutencao', 'descricao', 'data', 'data_up', 'status_chamado', 'usuario']

