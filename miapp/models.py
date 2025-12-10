from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    TIPO_CHOICES = [
        ('comida', 'Comida'),
        ('batido', 'Batido'),
    ]
    
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    imagen_url = models.URLField(max_length=500, blank=True)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titulo

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    video_url = models.URLField(max_length=500)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
