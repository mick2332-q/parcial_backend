from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10) # Podrías considerar un ChoiceField para sexo
    descripcion = models.TextField(blank=True, null=True) # TextField para descripciones largas, y opcional
    imagen = models.FileField(upload_to='animal_images/', blank=True, null=True) # Los archivos se subirán a media/animal_images/
    fecha_registro = models.DateField(auto_now_add=True) # Se establece automáticamente al crear

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"
        ordering = ['-fecha_registro'] # Ordena por fecha de registro descendente por defecto

    def __str__(self):
        return f"{self.nombre} ({self.especie})"