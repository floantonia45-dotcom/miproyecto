from django.contrib import admin
from .models import Receta, Articulo

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'usuario', 'fecha_creacion']
    list_filter = ['tipo', 'fecha_creacion']
    search_fields = ['titulo', 'ingredientes']

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion']
    search_fields = ['titulo', 'descripcion']