from django.urls import path, include
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('registrar/', views.registrar, name='registrar'),
    ]

