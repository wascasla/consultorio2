# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Historia_medica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_historia', models.DateTimeField()),
                ('diagnostico', models.CharField(max_length=500)),
                ('tratamiento', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField()),
                ('domicilio', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rel_Med_Esp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mat_especialidad', models.IntegerField()),
                ('especialidad', models.ForeignKey(to='gturnos.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('persona_ptr', models.OneToOneField(to='gturnos.Persona', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('mat_profesional', models.IntegerField()),
                ('organizaciones', models.ManyToManyField(to='gturnos.Organizacion')),
            ],
            bases=('gturnos.persona',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(to='gturnos.Persona', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('fecha_inicio', models.DateField()),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('perimetro_enc', models.IntegerField()),
            ],
            bases=('gturnos.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(to='gturnos.Sexo'),
        ),
        migrations.AddField(
            model_name='turno',
            name='medico',
            field=models.ForeignKey(to='gturnos.Medico'),
        ),
        migrations.AddField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(to='gturnos.Paciente'),
        ),
        migrations.AddField(
            model_name='rel_med_esp',
            name='medico',
            field=models.ForeignKey(to='gturnos.Medico'),
        ),
        migrations.AddField(
            model_name='historia_medica',
            name='medico',
            field=models.ForeignKey(to='gturnos.Medico'),
        ),
        migrations.AddField(
            model_name='historia_medica',
            name='paciente',
            field=models.ForeignKey(to='gturnos.Paciente'),
        ),
    ]
