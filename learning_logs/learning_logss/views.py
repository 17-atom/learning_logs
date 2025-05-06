# Create your views here.
from django.shortcuts import render, redirect
from .models import Tema, Entrada
from .forms import TemaForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """Pagina de Inicio de learning_logss"""
    return render(request, 'learning_logss/index.html')

def comprobar_propietario_tema(request):
    return Tema.objects.filter(propietario=request.user).order_by('agregar_dia')

@login_required
def temas(request):
    """Mostrar un solo tema y sus entradas"""
    temas = comprobar_propietario_tema(request)
    contexto = {'temas': temas}
    return render(request, 'learning_logss/temas.html', contexto)

@login_required
def tema(request, tema_id):
    """Mostramos un solo tema y todas sus entradas"""
    tema = Tema.objects.get(id=tema_id)
    #Este codigo asegura de que el tema pertenezca al usuario actual
    if tema.propietario != request.user:
        raise Http404

    entradas = tema.entrada_set.order_by('-date_add')
    context = {'tema':tema, 'entradas':entradas}
    return render(request, 'learning_logss/tema.html', context)

@login_required
def nuevo_tema(request):
    """Agregar un nuevo tema"""
    if request.method != 'POST':
        #No se enviaron los datos; crear un formulario en blanco
        formulario = TemaForm()
    else:
        #Datos POST enviados; procesar datos.
        formulario = TemaForm(data=request.POST)
        if formulario.is_valid():
            nuevo_tema = formulario.save(commit=False)
            nuevo_tema.propietario = request.user
            nuevo_tema.save()
            return redirect('learning_logss:temas')
    
    contexto = {'formulario': formulario}
    return render(request, 'learning_logss/nuevo_tema.html', contexto)

@login_required
def nueva_entrada(request, tema_id):
    """Agregar una nueva entrada para un tema en particular"""
    tema = Tema.objects.get(id=tema_id)

    if tema.propietario != request.user:
        raise Http404

    if request.method != 'POST':
        formulario = EntryForm()
    else:
        formulario = EntryForm(data=request.POST)
        if formulario.is_valid():
            nueva_entrada = formulario.save(commit=False)
            nueva_entrada.tema = tema
            nueva_entrada.save()
            return redirect('learning_logss:tema', tema_id=tema_id)
    
    contexto = {'tema': tema, 'formulario': formulario}
    return render(request, 'learning_logss/nueva_entrada.html', contexto)
    
@login_required
def editar_entrada(request, entrada_id):
    """Editar una entrada existente"""
    entrada = Entrada.objects.get(id=entrada_id)
    tema = entrada.tema

    #Protegemos la pagina de editar entrada.
    if tema.propietario != request.user:
        raise Http404

    if request.method != 'POST':
        #Solicitud inicial; prerellene el formulario con entrada actual
        formulario = EntryForm(instance=entrada)
    else:
        #Datos POST enviados, procesar datos.
        formulario = EntryForm(instance=entrada, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('learning_logss:tema', tema_id=tema.id)
    contexto = {'entrada': entrada, 'tema':tema, 'formulario':formulario}
    return render(request, 'learning_logss/editar_entrada.html', contexto)

