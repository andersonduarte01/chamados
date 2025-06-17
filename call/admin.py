from django.contrib import admin

from .models import Chamada

# Register your models here.

@admin.register(Chamada)
class ChamadaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'get_usuario_nome', 'status_chamado', 'data')

    def get_usuario_nome(self, obj):
        return obj.usuario.nome if obj.usuario else '---'
    get_usuario_nome.short_description = 'Usuário'