# Generated by Django 2.2 on 2019-11-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20191018_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='id_evento',
        ),
        migrations.AddField(
            model_name='evento',
            name='fotos',
            field=models.FileField(blank=True, null=True, upload_to='Fotografias'),
        ),
        migrations.DeleteModel(
            name='Fotografias',
        ),
        migrations.DeleteModel(
            name='Galeria',
        ),
    ]