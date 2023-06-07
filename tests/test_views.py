from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from scraper.models import Busqueda_nombres, Correciones
from predict.models import Predicciones
from iris.urls import Login


class Test_Views_Logout(TestCase):

    def test_login(self):
        cliente = Client()
        response = cliente.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_home_logout(self):
        cliente = Client()
        response = cliente.get(reverse('scraper:home'))
        self.assertEquals(response.status_code, 302)

    def test_cargar_archivo_logout(self):
        cliente = Client()
        response = cliente.get(reverse('scraper:cargar_archivo'))
        self.assertEquals(response.status_code, 302)

    def test_mostrar_DB_logout(self):
        cliente = Client()
        response = cliente.get(reverse('scraper:mostrar_DB'))
        self.assertEquals(response.status_code, 302)

    def test_predicciones_logout(self):
        cliente = Client()
        response = cliente.get(reverse('predict:predicciones'))
        self.assertEquals(response.status_code, 302)

    def test_listar_predicciones_logout(self):
        cliente = Client()
        response = cliente.get(reverse('predict:listar_predicciones'))
        self.assertEquals(response.status_code, 302)


class Test_View_login(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.user = User.objects.create_superuser('test_admin', '', 'test_admin')
        self.cliente.login(username='test_admin', password='test_admin')

        self.home_url = reverse('scraper:home')
        self.cargar_archivo_url = reverse('scraper:cargar_archivo')
        self.mostrar_DB_url = reverse('scraper:mostrar_DB')

    def test_home_GET(self):
        response = self.cliente.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'buscar.html')

    def test_cargar_archivo_GET(self):
        response = self.cliente.get(self.cargar_archivo_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cargar_archivo.html')

    def test_mostrar_DB_GET(self):
        response = self.cliente.get(self.mostrar_DB_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'visualizacion2.html')

    def test_predicciones_GET(self):
        response = self.cliente.get(reverse('predict:predicciones'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'predicciones.html')

    def test_listar_predicciones_GET(self):
        response = self.cliente.get(reverse('predict:listar_predicciones'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'visualizacion.html')

    