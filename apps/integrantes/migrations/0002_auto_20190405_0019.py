# Generated by Django 2.2 on 2019-04-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]