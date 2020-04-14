# Generated by Django 2.2 on 2019-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=45)),
                ('nombre', models.CharField(max_length=45)),
                ('escuela', models.CharField(choices=[('ecbti', 'ECBTI'), ('otra', 'OTRA'), ('otra1', 'OTRA1')], max_length=45)),
                ('tipo', models.CharField(choices=[('semillero', 'Semillero'), ('grado', 'Grado')], max_length=45)),
                ('fecha_creacion', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
