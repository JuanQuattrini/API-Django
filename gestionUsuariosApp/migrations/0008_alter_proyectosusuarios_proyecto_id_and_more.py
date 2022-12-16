# Generated by Django 4.1.3 on 2022-12-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0007_alter_proyectosusuarios_proyecto_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosusuarios',
            name='proyecto_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuariosApp.proyecto'),
        ),
        migrations.AlterField(
            model_name='proyectosusuarios',
            name='usuario_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuariosApp.usuario'),
        ),
    ]