from django.views.generic import View
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

class HomeView(View):
    def get(self, request, *args, **kwargs):
        contexts={

        }
        return render(request, "index.html", contexts)
    