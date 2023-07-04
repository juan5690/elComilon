from django.shortcuts import render
from .models import Cuenta, Pedidos
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def CrearCuenta(request):
    return render(request, 'app/CrearCuenta.html')

def sesion(request):
    return render(request, 'app/sesion.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def mensajePago(request):
    return render(request, 'app/mensajePago.html')

def agregar_cuenta(request):
    
    data={
        'form':cuentaForm() 
    }
    
    if request.method =='POST':
        formulario = cuentaForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="cuenta creada exitosamente!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/personas/agregar_persona.html', data)

def agregar_pedido(request):
    
    data={
        'form':pedidoForm() 
    }
    
    if request.method =='POST':
        formulario = pedidoForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="pedido realizado exitosamente, su pedido llegara en 15 minutos!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/pedidos/agregar_pedido', data)