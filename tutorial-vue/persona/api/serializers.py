from .models import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'  # Esto incluirá todos los campos del modelo
