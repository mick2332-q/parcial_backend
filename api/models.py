from django.db import models

class Mascota(models.Model):
    imagen = models.FileField(upload_to='mascotas/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10) # Podrías considerar un ChoiceField para sexo
    descripcion = models.TextField(blank=True, null=True) # TextField para descripciones largas, y opcional
    fecha_registro = models.DateField(auto_now_add=True) # Se establece automáticamente al crear

    def __str__(self):
        return f"{self.nombre} ({self.especie})"