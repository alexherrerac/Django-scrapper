from django.contrib import admin
from django.db.models.base import Model
from .models import Predicciones
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PrediccionesResources(resources.ModelResource):
    class Meta:
        model = Predicciones

class PrediccionesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ["nombre", "universidad", "profesion"]
    list_display = ("nombre", "universidad", "profesion", "ciudad", "cliente", "fecha",)
    resource_class = PrediccionesResources

admin.site.register(Predicciones, PrediccionesAdmin)
