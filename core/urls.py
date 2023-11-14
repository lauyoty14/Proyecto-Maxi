#from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path('barberia/',include('barberia.urls', namespace="barberia")),
    path('api/', include('barberia.api.urls')),  # Agrega la inclusión de las URLs de tu aplicación aquí
]

