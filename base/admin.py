from django.contrib import admin
from .models import Cliente, Repuesto, TipoReparacion  , TipoRepuesto
# Register your models here.

admin.site.register(Cliente)
admin.site.register(TipoRepuesto)
admin.site.register(Repuesto)
admin.site.register(TipoReparacion)