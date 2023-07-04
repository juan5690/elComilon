from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('sesion/', sesion, name='sesion'),
    path('CrearCuenta/', CrearCuenta, name='CrearCuenta'),
    path('mensajePago', mensajePago, name='mensajePago'),
    path('agregar_cuenta/', agregar_cuenta, name='agregar_cuenta'),
    path('agregar_pedido/', agregar_pedido, name='agregar_pedido')
]