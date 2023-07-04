from django.contrib import admin
from .models import Cuenta, Pedidos, Productos
# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Pedidos)
admin.site.register(Productos)