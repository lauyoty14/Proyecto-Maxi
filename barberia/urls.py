from core.urls import path
from .views import BarberiaListView, BarberiaCreateView

app_name="barberia"

urlpatterns = [
    path('', BarberiaListView.as_view(), name="home"),
    path("create/", BarberiaCreateView.as_view(), name="create")
]



