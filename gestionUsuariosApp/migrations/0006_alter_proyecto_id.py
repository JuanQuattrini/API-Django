# Generated by Django 4.1.3 on 2022-12-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0005_alter_proyecto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
