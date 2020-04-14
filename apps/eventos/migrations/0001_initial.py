# Generated by Django 2.1.7 on 2019-05-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integrantes', '0004_merge_20190427_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=45)),
                ('nombre', models.CharField(max_length=45)),
                ('lugar', models.CharField(max_length=45)),
                ('tipo', models.CharField(choices=[('taller', 'Taller'), ('capac', 'Capac'), ('wordshop', 'WordShop')], max_length=45)),
                ('fecha_creacion', models.DateField()),
                ('lider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='integrantes.Integrante')),
            ],
        ),
    ]