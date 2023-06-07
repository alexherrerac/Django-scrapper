from django.test import SimpleTestCase
from django.urls import reverse, resolve
from usuario.views import Login
from scraper.views import home, guardar_cambio, cargar_archivo, descargar_csv, mostrar_DB
from predict.views import predicciones, listar_predicciones, procesar_prediccion


class Test_Url(SimpleTestCase):

    def test_login_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, Login)
        
    def test_home_resolved(self):
        url = reverse('scraper:home')
        self.assertEquals(resolve(url).func, home)
    
    def test_guardar_cambio_resolved(self):
        url = reverse('scraper:guardar_cambio')
        self.assertEquals(resolve(url).func, guardar_cambio)

    def test_cargar_archivo_resolved(self):
        url = reverse('scraper:cargar_archivo')
        self.assertEquals(resolve(url).func, cargar_archivo)
    
    def test_descargar_csv_resolved(self):
        url = reverse('scraper:descargar_csv')
        self.assertEquals(resolve(url).func, descargar_csv)

    def test_mostrar_DB_resolved(self):
        url = reverse('scraper:mostrar_DB')
        self.assertEquals(resolve(url).func.view_class, mostrar_DB)


    def test_predicciones_resolved(self):
        url = reverse('predict:predicciones')
        self.assertEquals(resolve(url).func.view_class, predicciones)

    def test_listar_predicciones_resolved(self):
        url = reverse('predict:listar_predicciones')
        self.assertEquals(resolve(url).func.view_class, listar_predicciones)

    def test_procesar_prediccion_resolved(self):
        url = reverse('predict:procesar_prediccion')
        self.assertEquals(resolve(url).func, procesar_prediccion)
