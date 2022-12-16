from rest_framework import serializers
from gestionUsuariosApp.models import Proyecto, Usuario, ProyectosUsuarios, Sesiones


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Proyecto
        fields = ('id','nombre','activo')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Usuario
        fields = ('id','username','password','nombre','apellido','telefono','email','tipo','activo')

class ProyectoUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ProyectosUsuarios
        fields = ('id','usuarioid','proyectoid','activo')


class ListoProyectoUsuariosSerializer(serializers.ModelSerializer):
    usuarioid = serializers.StringRelatedField()
    proyectoid = serializers.StringRelatedField()
    class Meta:
        model  = ProyectosUsuarios
        fields = ('id','usuarioid','proyectoid','activo')  

class SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fiels = '__all__'    

class UsuarioLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fiels = '__all__'