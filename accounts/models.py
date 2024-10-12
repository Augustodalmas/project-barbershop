from django.db import models
from django.contrib.auth.models import AbstractUser
from barbershop.models import Barbershop


GeneroMasc = "Masculino"
GeneroFem = "Feminino"
GeneroOutro = "Outros"

Generos = [
    ("Masculino", "Masculino"),
    ("Feminino", "Feminino"),
    ("Outros", "Outros"),
]


class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True)
    numero_telefone = models.CharField(
        max_length=15, blank=True, null=True, default="(00)00000-0000")
    genero = models.CharField(choices=Generos, max_length=10, default="Outros")
    fotos = models.ImageField(upload_to='fotos/', null=True)

    def __str__(self):
        return self.username


class Barbeiro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, default="000.000.000-00", blank=True)
    barbershop = models.ForeignKey(
        Barbershop, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario.username


class Proprietário(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(
        Barbershop, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario.username
