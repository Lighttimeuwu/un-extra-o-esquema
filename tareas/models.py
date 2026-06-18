from django.db import models

class Tarea(models.Model):
    # El título de la tarea (un texto corto de hasta 200 caracteres)
    titulo = models.CharField(max_length=200)
    
    # Si la tarea está hecha o no (falso por defecto al crearla)
    completada = models.BooleanField(default=False)
    
    # Guarda la fecha y hora exacta en la que se creó la tarea automáticamente
    creada_en = models.DateTimeField(auto_now_add=True)

    # Esto sirve para que en el panel de control se vea el nombre de la tarea y no un texto genérico
    def __str__(self):
        return self.titulo