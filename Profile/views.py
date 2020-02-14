from django.shortcuts import render
from rest_framework.views import APIView
#Importar modelo
from Profile.models import *
from rest_framework.response import Response
#Importar Serializer
from Profile.serializer import *
from rest_framework import status




class CiudadList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = ModelCiudad.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = ModelGenero.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = ModelOcupacion.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = ModelEstado.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = ModelEstadoCivil.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProfileList2(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get(self,request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objectos
        serializer = ProfilieSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfilieSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
