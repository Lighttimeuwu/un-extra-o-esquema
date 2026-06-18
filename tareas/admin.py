from django.contrib import admin
from .models import Tarea

# Registramos el modelo Tarea para que aparezca en el panel de control
admin.site.register(Tarea)