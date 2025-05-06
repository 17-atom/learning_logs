from django.urls import path
from . import views

app_name = 'learning_logss'

urlpatterns=[
    #Pagina Principal
    path('', views.index, name='index'),
    path('temas/', views.temas, name='temas'),
    #Pagina de detalles para un solo tema
    path('temas/<int:tema_id>/', views.tema, name='tema'),
    path('nuevo_tema/', views.nuevo_tema, name='nuevo_tema'),
    #Pagina para agregar una nueva entrada
    path('nueva_entrada/<int:tema_id>/', views.nueva_entrada, name='nueva_entrada'),
    #Pagina para editar una entrada
    path('editar_entrada/<int:entrada_id>/', views.editar_entrada, name='editar_entrada'),
]