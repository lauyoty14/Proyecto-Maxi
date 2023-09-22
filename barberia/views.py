from django.shortcuts import get_object_or_404, render , redirect
from django.views.generic.base import View
from .forms import TurnoCreateForm
from .models import Turno

# Create your views here.
class BarberiaListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, "barberia.html", context)

class BarberiaCreateView(View):
    def get(self, request, *args, **kwargs):
        Form=TurnoCreateForm()
        context={
            'form':Form
        }
        return render(request, "SacarTurno.html",context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = TurnoCreateForm(request.POST)
            if form.is_valid():
                especialidad = form.cleaned_data.get('especialidad')
                servicio = form.cleaned_data.get('servicio')
                fecha = form.cleaned_data.get('fecha')
                profesional = form.cleaned_data.get('profesional')
                hora = form.cleaned_data.get('hora')              
                
                t, created = Turno.objects.get_or_create(especialidad=especialidad, servicio=servicio, fecha=fecha, profesional=profesional, hora=hora)
                t.save()
                return redirect('barberia:home')
        context={ 
        }
        return render(request, 'SacarTurno.html',context)
