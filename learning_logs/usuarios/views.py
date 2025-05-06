from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def salir(request):
    """Cerrar sesión del usuario."""
    logout(request)
    return redirect('usuarios:login')

def registrar(request):
    """Registrar nuevo usuario"""
    if request.method != 'POST':
        #Mostrar formulario de registro en blanco
        formulario = UserCreationForm
    else:
        formulario = UserCreationForm(data=request.POST)
        if formulario.is_valid():
            nuevo_usuario = formulario.save()
            #Iniciar sesión como el nuevo usuario y redirigir a la pagina de login
            login(request, nuevo_usuario)
            return redirect('usuarios:login')

    #Mostrar formulario en blanco o inválido
    contexto = {'formulario': formulario}
    return render(request, 'registration/registrar.html', contexto)