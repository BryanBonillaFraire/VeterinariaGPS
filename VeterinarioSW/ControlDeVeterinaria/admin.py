from django.contrib import admin
from .models import Propietario, Mascota, PagoServicio, Cita, Expediente, Producto, PagoServicio, Proveedor, Comprador, Factura, PagoProducto

admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(PagoServicio)
admin.site.register(Cita)
admin.site.register(Expediente)
admin.site.register(Producto)
admin.site.register(PagoProducto)
admin.site.register(Proveedor)
admin.site.register(Comprador)
admin.site.register(Factura)


