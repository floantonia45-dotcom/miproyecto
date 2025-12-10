from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # AUTENTICACIÓN
    path('register/', views.register_view, name='register'),
    path('acceso/', views.index2, name='index2'),

    # PÁGINAS
    path('historia/', views.index3, name='index3'),
    path('recetas/', views.index4, name='index4'),
    path('mis-recetas/', views.index5, name='index5'),

    # RUTAS FIJAS (tus páginas “plantilla”)
    path('editar-smoothie/', views.index6, name='index6'),
    path('editar-sopa/', views.index7, name='index7'),
    path('crear-batido/', views.index8, name='index8'),

    # ✅ ESTA ES LA RUTA QUE USA EL BOTÓN "CREAR"
    path('crear-router/', views.crear_router, name='crear_router'),

    # CRUD DE RECETAS DEL USUARIO (sin duplicar names)
    path('editar-receta/<int:id>/', views.editar_receta, name='editar_receta'),
    path('eliminar-receta/<int:id>/', views.confirmar_eliminar, name='confirmar_eliminar'),
    path('eliminar-receta/<int:id>/confirmar/', views.eliminar_receta, name='eliminar_receta'),
]
