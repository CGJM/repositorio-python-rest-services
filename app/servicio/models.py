import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from django.db import models


class Empleado (models.Model):
    nombreCompleto=models.CharField(max_length=35)
    clave=models.CharField(max_length=8)
    rol=models.CharField(max_length=35)
    telefono=models.CharField(max_length=35)
    edad=models.CharField(max_length=35)
    genero=models.CharField(max_length=35)
    salario=models.CharField(max_length=10)
