from django.db import models

# Create your models here.
class Turno(models.Model):
    fecha=models.DateField(max_length=50)
    especialidad=models.CharField(max_length=250)
    servicio=models.CharField(max_length=250)
    profesional=models.CharField(max_length=250)
    hora=models.TimeField(max_length=50)
