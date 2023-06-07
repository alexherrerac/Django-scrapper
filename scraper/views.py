import pandas as pd
import csv
import openpyxl
import joblib
from django.http import JsonResponse
from django.http import HttpResponse
from threading import Thread
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from scraper.models import *
from .pages import *

@login_required(login_url='/accounts/login/')
def home(request):
    resultado = None
    try:
        limpiar()
        if 'nombre' in request.POST:
            name = request.POST.get('nombre')
            if (name.isspace() or len(name) <= 10):
                resultado = None
            else:
                buscar(name)
                cliente = prediccion(profesion)
                resultado = zip(nombre, universidad, profesion, ciudad, cliente)
                guardar_todo(cliente)
    except:
        return render(request, 'buscar.html', {'resulta': "Nombre no encontrado"})
    return render(request, 'buscar.html', {'resultado': resultado})


def buscar(valor: str):
    for pag in paginas:
        hilo = Thread(target=pag, args=(valor,))
        hilo.start()
        threads.append(hilo)
    for hilos in threads:
        hilos.join()


def prediccion(profesion: str):
    # Carga el vectorizador y el modelo ML
    modelo = joblib.load('guardar_prueba.joblib')
    vectorizador = joblib.load('bagof.joblib')
    # Vectoriza las palabras y hace la prediccion
    vector = vectorizador.transform(profesion)
    cliente = modelo.predict(vector)
    return cliente


def guardar_todo(cliente):
    lista = zip(nombre, universidad, profesion, ciudad, cliente)
    Busqueda_nombres.objects.bulk_create([Busqueda_nombres(**{'nombre' : registro[0], 'universidad' : registro[1],
            'profesion' : registro[2], 'ciudad' : registro[3], 'cliente' : registro[4]}) for registro in lista])


def guardar_cambio(request):
    if request.POST.get('action') == 'post':
        nombres = request.POST.get('nombres')
        universidades = request.POST.get('universidad')
        profesiones = request.POST.get('profesion')
        ciudades = request.POST.get('ciudad')
        clientes = request.POST.get('cliente')

        Correciones.objects.create(nombre=nombres, universidad=universidades, profesion=profesiones,
                                ciudad=ciudades, cliente=clientes)
        
        return JsonResponse({'res': "Cambio realizado"}, safe=False)


@login_required(login_url='/accounts/login/')
def cargar_archivo(request):
    respuesta = None
    if request.method == 'POST':
        respuesta = upload(request)
    return render(request, "cargar_archivo.html", {'respuesta': respuesta})


def descargar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="resultados.csv"'

    writer = csv.writer(response, delimiter=",")
    writer.writerow(["Nombre", "Universidad", "Profesion", "Ciudad", "Cliente"])
    
    cliente = prediccion(profesion)
    for valor in zip(nombre, universidad, profesion, ciudad, cliente):
        writer.writerow([valor[0], valor[1], valor[2], valor[3], valor[4]])

    return response


def upload(request):
    try:
        limpiar()
        upload_file = request.FILES['document']
        if upload_file.name.endswith(".xlsx" or ".xls"):
            excel = openpyxl.load_workbook(upload_file, data_only=True)
            hoja = excel.active
            celdas = hoja["A{}:A{}".format(hoja.min_row, hoja.max_row)]

            for fila in celdas:
                valor = [celda.value for celda in fila]
                buscar(valor[0])
            cliente = prediccion(profesion)
            respuesta = {'respuesta': zip(nombre, universidad, profesion, ciudad, cliente)}
            guardar_todo(cliente)
            
        elif upload_file.name.endswith(".csv"):
            csv = pd.read_csv(upload_file)
            lista_nombres = csv["Nombre"]
                
            for item in lista_nombres:
                buscar(item)
            cliente = prediccion(profesion)
            respuesta = {'respuesta': zip(nombre, universidad, profesion, ciudad, cliente)}
            guardar_todo(cliente)

        else:
            respuesta = {'formato': "Tipo de archivo no permitido"}
        return respuesta
    except:
        return {'formato': "Por favor seleccionar un archivo valido"}
        

class mostrar_DB(ListView):
    model = Busqueda_nombres
    template_name = "visualizacion2.html"
    context_object_name = 'buscados'
    ordering = ['-fecha']
    paginate_by = 20
