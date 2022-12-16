# Generated by Django 4.1.3 on 2022-12-15 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0010_alter_proyectosusuarios_proyecto_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectosusuarios',
            name='proyecto_id',
        ),
        migrations.RemoveField(
            model_name='proyectosusuarios',
            name='usuario_id',
        ),
        migrations.AddField(
            model_name='proyectosusuarios',
            name='proyectoid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuariosApp.proyecto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectosusuarios',
            name='usuarioid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuariosApp.usuario'),
            preserve_default=False,
        ),
    ]
