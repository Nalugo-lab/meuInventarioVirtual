from django.db import models

# Create your models here.

class Teste(models.Model):

    name = models.CharField(max_length=25)