from django.urls import path
from base.views import clientes_views as views

urlpatterns = [ 
    path('cliente/',views.getCliente,name='obtener Clientes'),
    path('cliente/crear/', views.crearCliente, name='crear_cliente'),
    path('cliente/modificar/<int:cliente_id>/', views.modificarCliente, name='modificar_cliente'),
]
    
    
    



