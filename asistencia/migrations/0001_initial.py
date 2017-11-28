# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0002_auto_20171118_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField(verbose_name='Inicio: ')),
                ('fin', models.DateTimeField(verbose_name='Fin: ')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Registrado el: ')),
                ('trabajador', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='empleado.Trabajador')),
            ],
        ),
    ]