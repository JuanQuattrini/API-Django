from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from gestionUsuariosApp.models import Proyecto, Usuario, ProyectosUsuarios, Sesiones
from gestionUsuariosApp.serializers import ProyectoSerializer, UsuarioSerializer, ProyectoUsuariosSerializer
from gestionUsuariosApp.serializers import ListoProyectoUsuariosSerializer, SesionesSerializer, UsuarioLoginSerializer


# Create your views here.
class UsuarioLoginSerializer(generics.ListCreateAPIView):
    def post(self, request):
        username = request.GET.get("username")
        password = request.GET.get('password')
        miUsuario = Usuario.objects.filter(username = username , password = password).exists()
        if(miUsuario == True):
          return Response({'message': 'Habilitado'}, status = status.HTTP_200_OK)
        else:
          return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)    
    serializer_class = UsuarioLoginSerializer


class ProyectosList(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ProyectosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProyectosUsuariosList(generics.ListCreateAPIView):
    queryset = ProyectosUsuarios.objects.all()
    serializer_class = ProyectoUsuariosSerializer

class ProyectosUsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProyectosUsuarios.objects.all()
    serializer_class = ProyectoUsuariosSerializer

class ListoProyectoUsuariosList(generics.ListCreateAPIView):
    queryset = ProyectosUsuarios.objects.all()
    serializer_class = ListoProyectoUsuariosSerializer

class SesionesList(generics.ListCreateAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer

class SesionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer
    