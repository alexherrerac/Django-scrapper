from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "scraper"

urlpatterns = [
    path('', views.home, name='home'),
    path('guardar_cambio/', views.guardar_cambio, name='guardar_cambio'),
    path('cargar_archivo/', views.cargar_archivo, name='cargar_archivo'),
    path('cargar_archivo/descargar_csv/', views.descargar_csv, name='descargar_csv'),
    path('visualizacion2/', login_required(views.mostrar_DB.as_view()), name='mostrar_DB'),
]