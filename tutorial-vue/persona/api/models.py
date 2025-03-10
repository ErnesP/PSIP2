from django.db import models

class Persona(models.Model):
    # Definición de los campos
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email único para cada persona

    class Meta:
        ordering = ['id']  # Ordenar los resultados por el campo id en forma creciente

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.email})'
