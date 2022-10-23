# Generated by Django 4.0.4 on 2022-07-31 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'calle',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion_indigena.estado')),
            ],
            options={
                'verbose_name': 'municipio',
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion_indigena.municipio')),
            ],
            options={
                'verbose_name': 'Parroquia',
            },
        ),
        migrations.CreateModel(
            name='SectorBarrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion_indigena.parroquia')),
            ],
            options={
                'verbose_name': 'sector o barrio',
            },
        ),
    ]
