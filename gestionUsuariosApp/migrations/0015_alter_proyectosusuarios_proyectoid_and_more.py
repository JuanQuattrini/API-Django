# Generated by Django 4.1.3 on 2022-12-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0014_alter_proyectosusuarios_proyectoid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosusuarios',
            name='proyectoid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyectosusuarios',
            name='usuarioid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
