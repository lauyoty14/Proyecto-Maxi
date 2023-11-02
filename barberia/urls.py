from django.urls import path, include
from .views import BarberiaListView, BarberiaCreateView
from barberia.api.router import router_turnos
app_name="barberia"

urlpatterns = [
    path('', BarberiaListView.as_view(), name="home"),
    path("create/", BarberiaCreateView.as_view(), name="create"),
    path("api/", include(router_turnos.urls ))
]

