from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(verbose_name='Nome', max_length=150)
    escola = models.CharField(verbose_name='Escola', max_length=200)
    inep = models.CharField(verbose_name='Inep', max_length=20, unique=True)
    is_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.nome