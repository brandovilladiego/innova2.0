# Generated by Django 2.2 on 2020-02-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_proyecto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
