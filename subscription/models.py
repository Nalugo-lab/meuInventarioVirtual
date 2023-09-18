from django.db import models
from authentication.models import Client


class Subscription(models.Model):
    title = models.CharField(max_length=64, verbose_name='Assinatura')
    base_price = models.FloatField(max_length=16, verbose_name='Preço base')
    period = models.IntegerField(verbose_name='Período (em meses)')
    description = models.CharField(max_length=512, verbose_name='Descrição')
    subscription = models.ManyToManyField(Client, through="Client_subscription")


class Subscription_historic(models.Model):
    payment_date=models.DateField(verbose_name='Data da transação')
    end_date=models.DateField(verbose_name='Data de expiração')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)


class Client_subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    automatic = models.BooleanField(verbose_name='Automático')
    charge_day = models.IntegerField(verbose_name='Dia de renovação')
