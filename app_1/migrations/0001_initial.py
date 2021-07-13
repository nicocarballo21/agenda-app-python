# Generated by Django 3.1.5 on 2021-02-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.SmallIntegerField()),
                ('dni', models.IntegerField()),
                ('provincia', models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Cordoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Rios'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquen'), ('Río Negro', 'Rio Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucuman')], max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]