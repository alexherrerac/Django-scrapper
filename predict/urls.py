from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('predicciones/', login_required(views.predicciones.as_view()), name='predicciones'),
    path('prediccion/', views.procesar_prediccion, name='procesar_prediccion'),
    path('visualizacion/', login_required(views.listar_predicciones.as_view()), name='listar_predicciones'),
]