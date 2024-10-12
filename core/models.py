from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

"""
Criação do banco de dados de inscrição dos planos para os barbeiros
Plan é utilizados para criar um plano, definindo nome, preço e moeda
Subscription é utilizado para definir qual usuário possui qual plano, no caso, ao pagar pelo plano será o usuário será linkado ao plano
"""


class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Barbershop(models.Model):
    name = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14)
    andress = models.CharField(max_length=255)
    telephone = models.CharField(max_length=13)
    service = models.ManyToManyField(
        Service, related_name="Service_Barbershop")
    email = models.EmailField()
    is_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='estabelecimentos/', null=True)
    description = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name_plan = models.CharField(max_length=255)
    id_plan = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="R$")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_plan


class Subscription(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription_id = models.CharField(max_length=255, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    next_billing_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} - {self.plan.name_plan}'
