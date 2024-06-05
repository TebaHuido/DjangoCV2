from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(alumno)
admin.site.register(clase)
admin.site.register(curso)
admin.site.register(asistencia)