from django.urls import path
from .views import (
    Listado_listView,
    Create_contacto,
    Update_contacto,
    Delete_contacto,
)


"""
    urls.py: Se encarga de gestionar las url de cada pagina dentro de la aplicacion.

"""

app_name = 'app'
urlpatterns = [
    path('', Listado_listView.as_view(), name='listar'),
    path('agregar-contacto', Create_contacto.as_view(), name='agregar'),
    path('editar-contacto/<pk>/', Update_contacto.as_view(), name='editar'),
    path('eliminar-contacto/<pk>/', Delete_contacto.as_view(), name='eliminar'),

]
