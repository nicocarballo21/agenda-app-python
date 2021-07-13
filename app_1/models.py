from django.db import models

provincias_choice = [
    ('Buenos Aires', 'Buenos Aires'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Cordoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Rios'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquen'),
    ('Río Negro', 'Rio Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucuman'),
]


class Registros(models.Model):
    """
        Clase encargadada de crear la base de datos que almacenara los contactos
        La clase representa una tabla dentro de la base de datos
        Cada item dentro de la clase representa un campo de datos dentro de la tabla

    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    edad = models.SmallIntegerField()
    dni = models.IntegerField()
    provincia = models.CharField(max_length=50, choices=provincias_choice)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
