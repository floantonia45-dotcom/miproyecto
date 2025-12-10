from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Receta, Articulo
from django.urls import reverse
from django.contrib.auth import login as auth_login

import json

def index1(request):
    return render(request, 'index1.html')

def index2(request):
    form_type = request.GET.get('form', 'login')
    
    if request.method == 'POST':
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index1')
            except User.DoesNotExist:
                pass
        
        elif 'register' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect('index1')
    
    return render(request, 'index2.html', {'form_type': form_type})

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    recetas = Receta.objects.all()
    comidas = recetas.filter(tipo='comida')
    batidos = recetas.filter(tipo='batido')
    return render(request, 'index4.html', {'comidas': comidas, 'batidos': batidos})

@login_required
def index5(request):
    recetas_usuario = Receta.objects.filter(usuario=request.user)
    return render(request, 'index5.html', {'recetas': recetas_usuario})

@login_required
def index6(request):
    return render(request, 'index6.html')

@login_required
def index7(request):
    return render(request, 'index7.html')

@login_required
def index8(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen_url = request.POST.get('imagenUrl')
        ingredientes = request.POST.get('ingredientes')
        preparacion = request.POST.get('preparacion')
        
        receta = Receta(
            titulo=nombre,
            tipo='batido',
            imagen_url=imagen_url,
            ingredientes=ingredientes,
            preparacion=preparacion,
            usuario=request.user
        )
        receta.save()
        return redirect('index5')
    
    return render(request, 'index8.html')

@login_required
def index9(request):
    return render(request, 'index9.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Buscar usuario por email
            user_obj = User.objects.get(email=email)
            
            # Autenticación usando username
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index5')  # ⬅️ LOGIN EXITOSO
        except User.DoesNotExist:
            pass
        
        # Si falló, volver al login
        return redirect(f"{reverse('index2')}?form=login")

    return redirect(f"{reverse('index2')}?form=login")

def logout_view(request):
    logout(request)
    return redirect('index1')

def register_view(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return redirect(f"{reverse('index2')}?form=register")

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return redirect(f"{reverse('index2')}?form=register")

# ⬇⬇⬇ AQUI VA BIEN UBICADA LA FUNCIÓN ⬇⬇⬇

@login_required
def editar_receta(request, id):
    receta = get_object_or_404(Receta, id=id, usuario=request.user)

    if request.method == "POST":
        receta.titulo = request.POST.get("titulo")
        receta.tipo = request.POST.get("tipo")
        receta.imagen_url = request.POST.get("imagen_url")
        receta.ingredientes = request.POST.get("ingredientes")
        receta.preparacion = request.POST.get("preparacion")
        receta = get_object_or_404(Receta, id=id, usuario=request.user)
        receta.save()

        return redirect('index5')

    return render(request, "editar_receta.html", {"receta": receta})

@login_required
def confirmar_eliminar(request, id):
    receta = get_object_or_404(Receta, id=id, usuario=request.user)
    return render(request, "index9.html", {"receta": receta})


@login_required
def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id, usuario=request.user)

    if request.method == "POST":
        receta.delete()
        return redirect('index5')

    # Si entra por GET por error, lo mando a index5
    return redirect('index5')

def crear_router(request):
    # Si el usuario está logueado → enviar a index5
    if request.user.is_authenticated:
        return redirect('index5')

    # Si NO está logueado → enviar al registro dentro de index2
    return redirect(f"{reverse('index2')}?form=register")
