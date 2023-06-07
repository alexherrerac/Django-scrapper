import joblib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.list import ListView 
from django.views.generic import TemplateView 
from .models import Predicciones

# Carga pagina para hacer predicciones
class predicciones(TemplateView):
    template_name = 'predicciones.html'


# Hace la prediccion de los datos ingresados
def procesar_prediccion(request):

    if request.POST.get('action') == 'post':

        # Recibe datos del cliente
        nombre = request.POST.get('nombre')
        universidad = request.POST.get('universidad')
        profesion = request.POST.get('profesion')
        ciudad = request.POST.get('ciudad')

        # Carga el vectorizador y el modelo
        model = joblib.load('modelo_clasificacion.joblib')
        bagofwords = joblib.load('vectorizador.joblib')

        # Vectoriza las palabras
        vector = bagofwords.transform([profesion])

        # Hace la prediccion
        cliente = model.predict(vector)[0]

        # Crea un objeto con los datos de la prediccion y lo guarda en la DB
        Predicciones.objects.create(nombre=nombre, universidad=universidad, profesion=profesion,
                                ciudad=ciudad, cliente=cliente)

        # Responde en formato JSON el resultado de la prediccion
        return JsonResponse({'cliente': cliente, 'nombre': nombre, 'universidad': universidad,
                            'profesion': profesion, 'ciudad': ciudad}, safe=False)


class listar_predicciones(ListView):
    model = Predicciones
    template_name = "visualizacion.html"
    context_object_name = 'listado'
    paginate_by = 20
    ordering = ['-fecha']
