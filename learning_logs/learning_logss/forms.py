from django import forms
from .models import Tema, Entrada

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['texto']
        labels = {'texto': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['texto']
        labels = {'texto':'Entrada'}
        widgets = {'texto': forms.Textarea(attrs={'cols':80})}
        
