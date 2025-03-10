from django.shortcuts import render

# Create your views here.
from .models import Persona
from .serializers import PersonaSerializer
from rest_framework import viewsets

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()  # Obtener todas las personas
    serializer_class = PersonaSerializer  # Usar el serializador definido anteriormente
