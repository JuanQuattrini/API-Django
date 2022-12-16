from django.urls import re_path as url
#from django.conf.urls import url


from . import views

urlpatterns = [
   url(r'^proyectos$', views.ProyectosList.as_view()),
   url(r'^proyectos/(?P<pk>[0-9]+)$', views.ProyectosDetail.as_view()),

   url(r'^usuarios$', views.UsuariosList.as_view()),
   url(r'^usuarios/(?P<pk>[0-9]+)$', views.UsuariosDetail.as_view()),

   url(r'^proyectosusuarios$', views.ProyectosUsuariosList.as_view()),
   url(r'^proyectosusuarios/(?P<pk>[0-9]+)$', views.ProyectosUsuariosDetail.as_view()),

   url(r'^proyectosusuarioslist$', views.ListoProyectoUsuariosList.as_view()),

   url(r'^sesiones$', views.SesionesList.as_view()),
   url(r'^sesiones/(?P<pk>[0-9]+)$', views.SesionesDetail.as_view()),

   url(r'^login$', views.UsuarioLoginSerializer.as_view()),

   

]