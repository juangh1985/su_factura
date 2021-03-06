# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mprima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='Materias Primas', upload_to='mprima/', verbose_name='imagen')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Producto')),
                ('pcosto', models.FloatField(blank=True, max_length=30, null=True, verbose_name='Precio de Costo')),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Registro')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('observacion', models.TextField(blank=True, max_length=30, null=True, verbose_name='Observacion')),
                ('activo', models.BooleanField(max_length=256, verbose_name='Activo')),
            ],
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='umedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Unidad de Medida')),
            ],
        ),
        migrations.AddField(
            model_name='mprima',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiaprima.tipo'),
        ),
        migrations.AddField(
            model_name='mprima',
            name='umedida',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiaprima.umedida'),
        ),
    ]
