# Generated by Django 2.2 on 2019-10-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombEsci', models.CharField(max_length=50, verbose_name='Estado Civil')),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estados Civiles',
            },
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEtni', models.CharField(max_length=50, verbose_name='Grupo Etnico')),
            ],
            options={
                'verbose_name': 'Grupo Etnia',
                'verbose_name_plural': 'Grupos Etnia',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombtiDo', models.CharField(max_length=50, verbose_name='Tipo de Documento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='tipoEstu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTi', models.CharField(max_length=50, verbose_name='Tipo Estudiante')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='tipoLogr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTilo', models.CharField(max_length=50, verbose_name='Tipo de logro')),
            ],
            options={
                'verbose_name': 'Logros',
                'verbose_name_plural': 'Logros obtenidos',
            },
        ),
    ]
