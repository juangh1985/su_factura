# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiaprima', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='existencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencia', models.CharField(blank=True, max_length=30, null=True, verbose_name='Existencia')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('materia', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiaprima.mprima')),
            ],
        ),
        migrations.CreateModel(
            name='movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(blank=True, max_length=30, null=True, verbose_name='Cantidad')),
                ('importe', models.CharField(blank=True, max_length=30, null=True, verbose_name='Importe')),
                ('pcosto', models.CharField(blank=True, max_length=30, null=True, verbose_name='Precio de Costo')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('materia', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiaprima.mprima')),
            ],
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo')),
            ],
        ),
        migrations.AddField(
            model_name='movimiento',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.tipo'),
        ),
    ]
