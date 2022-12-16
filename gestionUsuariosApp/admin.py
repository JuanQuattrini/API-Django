from django.contrib import admin
from gestionUsuariosApp.models import Proyecto, Usuario, ProyectosUsuarios, Sesiones

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","activo")
    search_fields=("id","nombre")

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("id","username","password","nombre","apellido","telefono","email","tipo","activo")
    search_fields=("id","username","password","nombre","apellido")

class ProyectosUsuariosAdmin(admin.ModelAdmin):
    list_display=("id","usuarioid","proyectoid","activo")
    search_fields=("id","usuarioid","proyectoid","activo") 

class SesionesAdmin(admin.ModelAdmin):
    list_display=("id","usuario","activo")
    search_fields=("id","usuario","activo") 

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ProyectosUsuarios, ProyectosUsuariosAdmin)
admin.site.register(Sesiones, SesionesAdmin)
