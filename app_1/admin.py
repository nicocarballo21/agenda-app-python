from django.contrib import admin
from .models import Registros


class RegisterAdmin(admin.ModelAdmin):
    """
        Clase encargada de administrar la pagina ADMIN
        Muestras los datos de la base de datos y a su vez muestra un campo
        de busquedad y filtros.

    """
    list_display = [
        'nombre',
        'apellido',
        'edad',
        'provincia',
        'dni',
    ]
    list_filter = ['edad', 'provincia']
    search_fields = ['nombre', 'apellido']


admin.site.register(Registros, RegisterAdmin)
