# Generated by Django 3.1 on 2020-11-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlDeVeterinaria', '0002_auto_20201121_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]