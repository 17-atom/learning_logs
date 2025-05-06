from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tema(models.Model):
    """Un tema sobre el que el usuario esta aprendiendo"""
    texto = models.CharField(max_length=200)
    agregar_dia = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Retorna una representación de cadena del modelo"""
        return self.texto

class Entrada(models.Model):
    """Algo especifico aprendido sobre un tema"""
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    texto = models.TextField()
    date_add = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entradas'
    
    def __str__(self):

        if len(self.texto) > 50:
            return (f" {self.texto[:50]}...")
        
        return self.texto[:]
