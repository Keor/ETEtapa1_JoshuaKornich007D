from django.db import models
from django.db.models.deletion import CASCADE
from django import forms

class Colaborador(models.Model):
    rut = models.CharField(primary_key=True,max_length=12,verbose_name='Rut del Colaborador')
    nomCompleto = models.CharField(max_length=100,verbose_name='Nombre Completo')
    fono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=100,verbose_name='Dirección')
    mail = models.CharField(max_length=50,verbose_name='Mail')
    pais = models.CharField(max_length=50,verbose_name='Pais')
    foto = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Foto de Colaborador')
    contrasena = models.CharField(max_length=20,verbose_name='Contraseña')

    def __str__(self):
        return(self.rut)