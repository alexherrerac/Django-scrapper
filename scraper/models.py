from django.db import models
from django.db.models.fields import CharField


class Busqueda_nombres(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre de la persona", max_length=30)
    universidad = models.CharField("Universidad", max_length=50)
    profesion = models.CharField("Profesion", max_length=80)
    ciudad = models.CharField("Ciudad de la Universidad", max_length=20)
    cliente = models.CharField("Posibilidad de cliente", max_length=10)
    fecha = models.DateTimeField("Fecha de registro", auto_now=True)

    class Meta:
        get_latest_by = "fecha"
        verbose_name_plural = "Nombres buscados"

    def __str__(self):
        return self.nombre

class Correciones(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre de la persona", max_length=30)
    universidad = models.CharField("Universidad", max_length=50)
    profesion = models.CharField("Profesion", max_length=80)
    ciudad = models.CharField("Ciudad de la Universidad", max_length=20)
    cliente = models.CharField("Posibilidad de cliente", max_length=10)
    fecha = models.DateTimeField("Fecha de registro", auto_now=True)

    class Meta:
        get_latest_by = "fecha"
        verbose_name_plural = "Correccion de predicciones"

    def __str__(self):
        return self.nombre
