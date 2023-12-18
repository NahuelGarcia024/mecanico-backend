from django.urls import path
from base.views import repuestos_views as views

urlpatterns = [ 
    path('repuesto/', views.getRepuesto, name='obtener Repuestos'),
    path('repuesto/crear/', views.crearRepuesto, name='crear_cliente'),
    path('repuesto/modificar/<int:repuesto_id>/', views.modificarRepuesto, name='modificar_Repuesto'),
    
    
]
    
    
    



