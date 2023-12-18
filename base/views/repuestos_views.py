import csv
from decimal import Decimal
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from base.models import Repuesto
from base.serializers import RepuestoSerializer
from rest_framework import status, viewsets
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def getRepuesto(request):
    repuestos = Repuesto.objects.all()
    serializer = RepuestoSerializer(repuestos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearRepuesto(request):
    serializer = RepuestoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def modificarRepuesto(request, repuesto_id):
    try:
        repuesto = Repuesto.objects.get(pk=repuesto_id)
    except Repuesto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RepuestoSerializer(Repuesto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)