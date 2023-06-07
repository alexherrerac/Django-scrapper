from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class Busqueda_nombresResources(resources.ModelResource):
    class Meta:
        model = Busqueda_nombres

class Busqueda_nombresAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ["nombre", "universidad", "profesion"]
    list_display = ("nombre", "universidad", "profesion", "ciudad", "cliente", "fecha",)
    resource_class = Busqueda_nombresResources


class CorrecionesResources(resources.ModelResource):
    class Meta:
        model = Correciones

class CorrecionesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ["nombre", "universidad", "profesion"]
    list_display = ("nombre", "universidad", "profesion", "ciudad", "cliente", "fecha",)
    resource_class = CorrecionesResources


admin.site.register(Correciones, CorrecionesAdmin)
admin.site.register(Busqueda_nombres, Busqueda_nombresAdmin)
