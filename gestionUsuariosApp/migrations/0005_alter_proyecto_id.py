# Generated by Django 4.1.3 on 2022-12-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0004_alter_proyecto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
