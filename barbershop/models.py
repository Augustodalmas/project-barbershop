from django.db import models
from core.models import Barbershop, Service
from django.conf import settings


class Barber(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, verbose_name="Nome Barbeiro")
    telephone = models.CharField(
        max_length=13, verbose_name="Telefone do Barbeiro")
    email = models.EmailField(verbose_name="E-mail do barbeiro")
    service = models.ManyToManyField(
        Service, related_name="Service_Barber", verbose_name="Serviços do Barbeiro")
    barbershop = models.ForeignKey(Barbershop, on_delete=models.CASCADE,
                                   related_name="Barber_Barbershop", default=None, null=True, blank=True)

    def __str__(self):
        return self.username
