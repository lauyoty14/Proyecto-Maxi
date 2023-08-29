from django import forms
from .models import Turno

class TurnoCreateForm(forms.ModelForm):
    class Meta: 
        model=Turno
        fields=("fecha","especialidad","servicio","profesional","hora")

