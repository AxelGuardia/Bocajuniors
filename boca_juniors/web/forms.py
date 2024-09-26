from django import forms
from .models import Novedades, Futbol, Indumentaria

class NovedadesForm(forms.ModelForm):
    class Meta:
        model = Novedades
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),
        }

class FutbolForm(forms.ModelForm):
    class Meta:
        model = Futbol
        fields = '__all__'

class IndumentariaForm(forms.ModelForm):
    class Meta:
        model = Indumentaria
        fields = '__all__'
