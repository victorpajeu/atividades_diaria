from django.db import models


class Doctor(models.Model):
    name = models.CharField('Nome', null=False, max_length=200)
    age = models.IntegerField('Idade', null=False, )
    cpf = models.IntegerField('CPF', null=False)

