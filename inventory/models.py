from django.conf import settings
from django.db import models
from django.utils import timezone
from authentication.models import Client


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Criador"), on_delete=models.PROTECT)
    creation_datetime = models.DateTimeField(verbose_name=("date joined"), default=timezone.now)


class Inventory(models.Model):

    title = models.CharField(max_length=64)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Criador"), on_delete=models.PROTECT)
    creation_datetime = models.DateTimeField(verbose_name=("date joined"), default=timezone.now)


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    quantity = models.IntegerField()
    barcode=models.CharField(max_length=32)
    base_price=models.FloatField()
    commercial_price= models.FloatField()
    tag=models.ForeignKey(Tag, on_delete=models.PROTECT)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Criador"), on_delete=models.PROTECT)
    creation_datetime = models.DateTimeField(verbose_name=("date joined"), default=timezone.now)


class Transaction(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)


class Historic(models.Model):
    HISTORIC_STATUS = [
    (1, "Remove - transaction"),
    (2, "Remove - expiration date"),
    (3, "Remove - manual"),
    (4, "Add"),
    (5, "Devolution")
    ]

    datetime = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Criador"), on_delete=models.PROTECT)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    value = models.FloatField()
    status = models.IntegerField(choices=HISTORIC_STATUS)