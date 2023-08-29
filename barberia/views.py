from django.shortcuts import render
from django.views.generic.base import View
from .forms import TurnoCreateForm

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
        context={

        }
        return render(request, "SacarTurno.html",context)
