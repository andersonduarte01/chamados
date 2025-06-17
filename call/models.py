from django.db import models

from usuario.models import Usuario


# Create your models here.

class Chamada(models.Model):
    APARELHOS = [
        ('1', 'Computador'),
        ('2', 'Impressora'),
        ('3', 'Computador e Impresssora'),
        ('4', 'Outro'),
    ]

    STATUS = [
        ('1', 'AGUARDANDO'),
        ('2', 'FINALIZADO'),
        ('3', 'CANCELADO'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    manutencao = models.CharField(verbose_name='Manutenção', max_length=30, choices=APARELHOS)
    descricao = models.TextField(verbose_name='Descrição')
    data = models.DateTimeField(auto_now_add=True)
    data_up = models.DateTimeField(auto_now=True)
    status_chamado = models.CharField(verbose_name='Chamado', choices=STATUS, max_length=30, default='1')

    def __str__(self):
        return self.descricao

