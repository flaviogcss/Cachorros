from django.db import models

# Create your models here.
from dono.models import Dono


class Gatinho(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cores_pelo = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('PARDO', 'Pardo'),
        ('LARANJA', 'Laranja'),
        ('CINZA', 'Cinza'),
        ('TRICOLOR', 'Tricolor'),
        ('BEGE', 'Bege'),
    )
    cor = models.CharField(choices=cores_pelo, max_length=100)
    dono = models.ManyToManyField(Dono)
