# Generated by Django 4.1.3 on 2022-12-16 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuariosApp', '0016_alter_proyectosusuarios_proyectoid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField()),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuariosApp.usuario')),
            ],
        ),
    ]
