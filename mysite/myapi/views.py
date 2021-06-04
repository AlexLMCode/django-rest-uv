from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriaSerializer, EmpresaSerialier, EstadoSerializer, HeroSerializer, MunicipioSerializer
from .models import Categoria, Empresa, Estado, Hero, Municipio

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all().order_by('idestado')
    serializer_class = EstadoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('codigo_actividad')
    serializer_class = CategoriaSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all().order_by('nombre_municipio')
    serializer_class = MunicipioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('nombre_empresa')
    serializer_class = EmpresaSerialier
