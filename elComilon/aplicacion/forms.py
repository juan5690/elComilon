from django import forms
from .models import Cuenta, Pedidos

class cuentaForm(forms.ModelForm):
    
    class Meta:
        model=Cuenta
        fields=["rut","nombre","apellido"]
        
class pedidoForm(forms.ModelForm):
    
    class Meta:
        model=Pedidos
        fields=["nombre","direccion"]