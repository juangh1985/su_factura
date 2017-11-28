# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=256, null=True, verbose_name='Cliente')),
                ('correo', models.CharField(max_length=256, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=256, null=True, verbose_name='Telefono de Contacto')),
                ('direccion', models.CharField(max_length=256, null=True, verbose_name='Direccion')),
                ('imagen', models.ImageField(blank=True, upload_to='cliente/', verbose_name='imagen')),
                ('registro', models.DateTimeField(auto_now=True, verbose_name='Registrado')),
                ('estado', models.BooleanField(max_length=256, verbose_name='Activo')),
                ('empresa', models.BooleanField(max_length=256, verbose_name='Empresa')),
            ],
        ),
    ]