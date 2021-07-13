from django import forms
from .models import Registros
from django.forms import ValidationError
from crispy_forms.helper import FormHelper


class RegistroForm(forms.ModelForm):

    """
        Clase encargada de gestionar el formulario que realiza las altas de contactos a la base
        de datos.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.form_show_errors = True

    # declaracion del form
    class Meta:
        model = Registros
        fields = '__all__'

    # Validaciones
    ##########################################################################

    """
        clean_dni rescata el valor ingresado en el form e informa si ya existe en la
        base de datos,
        ademas valida que tenga longitud correcta.

        Ademas se agregan mas validaciones para otros campos como el nombre, apellido y edad.

    """

    def clean_dni(self):

        dni = self.cleaned_data['dni']
        len_dni = len(str(dni))
        existe = Registros.objects.filter(dni__iexact=dni).exists()

        if existe:
            raise ValidationError('Dni ya existente')
        if len_dni != 8:
            if len_dni > 8:
                faltan = len_dni - 8
                raise ValidationError(f'Longitud incorrecta, sobran {faltan} digitos.')
            else:
                faltan = 8 - len_dni
                raise ValidationError(f'Longitud incorrecta, faltan {faltan} digitos.')
        return dni

    nombre = forms.RegexField(
        regex="^[a-zA-Z]+$", error_messages={'invalid': 'Ingrese solo letras'})

    apellido = forms.RegexField(
        regex="^[a-zA-Z]+$", error_messages={'invalid': 'Ingrese solo letras'})

    edad = forms.IntegerField(max_value=100, min_value=0)


class EditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.form_show_errors = True

    # Declaracion del form
    class Meta:
        model = Registros
        fields = ['nombre', 'apellido', 'edad', 'provincia']

    # validaciones
    nombre = forms.RegexField(
        regex="^[a-zA-Z]+$", error_messages={'invalid': 'Ingrese solo letras'})

    apellido = forms.RegexField(
        regex="^[a-zA-Z]+$", error_messages={'invalid': 'Ingrese solo letras'})

    edad = forms.IntegerField(max_value=100, min_value=0)
