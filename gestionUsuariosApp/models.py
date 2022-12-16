from django.db import models


# Create your models here.

TIPO = (
    (0,'SuperUsuario'),
    (1,'Administrador'),
)
class Proyecto(models.Model):
    nombre = models.CharField(unique=True,max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    username = models.CharField(unique=True,max_length=15)
    password = models.CharField(max_length=8)
    nombre   = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email    = models.EmailField()
    tipo     = models.IntegerField(choices=TIPO)
    activo = models.BooleanField()

    def __str__(self):
        return self.username

class ProyectosUsuarios(models.Model):
    usuarioid  = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    proyectoid = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField()    

class Sesiones(models.Model):
    activo = models.BooleanField()     
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)


     
