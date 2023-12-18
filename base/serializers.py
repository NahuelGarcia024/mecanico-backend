from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Repuesto , TipoReparacion, TipoRepuesto
from rest_framework_simplejwt.tokens import RefreshToken

class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class TipoReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReparacion
        fields = '__all__'
        
class TipoRepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRepuesto
        fields = '__all__'
        
        