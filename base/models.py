from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    patente= models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=50, null=False, blank=False)
    dni = models.CharField(max_length=50, null=False, blank=False, default="0")
    
    def __str__(self):
        return self.nombre
    
class TipoReparacion(models.Model):
    nombre_tipo_repuesto = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre_tipo_repuesto

class TipoRepuesto(models.Model):
    nombre_tipo_repuesto = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre_tipo_repuesto
    
class Repuesto(models.Model):
    nombre_repuesto = models.CharField(max_length=50, null=False, blank=False)
    reparado = models.BooleanField(default=False)
    entrega = models.BooleanField(default=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=False, blank=False)
    id_tipo_reparacion = models.OneToOneField(TipoReparacion, on_delete=models.CASCADE, default="", null=False, blank=False)
    id_cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default="", null=False, blank=False)
    id_tipo_repuesto= models.OneToOneField(TipoRepuesto, on_delete=models.CASCADE, default="", null=False, blank=False)
    def __str__(self):
        return str(self.nombre_repuesto)