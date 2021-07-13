from django.urls import reverse_lazy
from .models import Registros
from .forms import RegistroForm, EditForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


class Listado_listView(ListView):
    """
        Clase encargada de listar y mostrar los contactos dentro de la pagina principal.
        Aplica el metodo get_context_data para realizar la busquedad de los contactos dentro de
        la base de datos.
            Devuelve un un diccionario con la data que sera mostrada en pantalla.
    """
    model = Registros
    template_name = 'App_1/listar_contactos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('buscar', ''). split(' ')
        contactos = Registros.objects.all()
        if search:
            for s in search:
                contactos = contactos.filter(Q(nombre__icontains=s) | Q(apellido__icontains=s))

        context['contacto'] = [{
            'instancia': contacto,
            # 'form': RegistroForm(instance=contacto)
        }
            for contacto in contactos
        ]
        print(context)
        return context


class Create_contacto(SuccessMessageMixin, CreateView):
    """
        Clase encargada de gestionar la creacion de nuevos contactos
        Tambien gestiona los mensajes correspondientes a la accion

    """

    form_class = RegistroForm
    template_name = 'App_1/agregar_contactos.html'
    success_url = reverse_lazy('app:listar')
    success_message = "Contacto creado con exito"


class Update_contacto(SuccessMessageMixin, UpdateView):
    """
        Clase encargada de grstionar la actualizacion de contactos ya existentes
        Tambien gestiona los mensajes correspondieste a la accion
    """
    form_class = EditForm
    template_name = 'App_1/editar_contactos.html'
    model = Registros
    success_message = 'Contacto editado'
    success_url = reverse_lazy('app:listar')


class Delete_contacto(SuccessMessageMixin, DeleteView):
    """
        Clase encargada de gestionar la eliminacion de contactos.
        Tambien gestiona los mensajes correspondieste a la accion
    """
    model = Registros
    success_url = reverse_lazy('app:listar')
