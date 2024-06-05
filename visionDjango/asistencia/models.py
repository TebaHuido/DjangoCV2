from django.db import models

# Create your models here.
class alumno(models.Model):
    id_alumno = models.PositiveIntegerField(unique=True) 
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class curso(models.Model):
    nombre= models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.nombre

class clase(models.Model):
    fecha =models.DateField()
    id_curso = models.ForeignKey(curso,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_curso) + str(self.fecha)
class asistencia(models.Model):
    alumno = models.ForeignKey(alumno,on_delete=models.CASCADE)
    clase =models.ForeignKey(clase,on_delete=models.CASCADE)
    asistio=models.BooleanField(default=False)