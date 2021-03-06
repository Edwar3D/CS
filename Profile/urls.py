from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Profile import views

urlpatterns = [
    re_path(r'profileList/$',views.ProfileList2.as_view()),
    re_path(r'ciudadList/$',views.CiudadList.as_view()),
    re_path(r'generoList/$',views.GeneroList.as_view()),
    re_path(r'ocupacionList/$',views.OcupacionList.as_view()),
    re_path(r'estadoList/$',views.EstadoList.as_view()),
    re_path(r'estadocivilList/$',views.EstadoCivilList.as_view()),
]