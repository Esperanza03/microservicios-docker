from django.db import models

class Estudiante(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    curso = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.rut} - {self.nombre_completo}"