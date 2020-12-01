from django.contrib import admin
from .models import Propietario, Mascota, PagoServicio, Cita, Account, Producto, PagoServicio, Proveedor, Comprador, Factura, PagoProducto, Vacunas, Cirugias, Enfermedades, Otros

admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(PagoServicio)
admin.site.register(Cita)
admin.site.register(Producto)
admin.site.register(PagoProducto)
admin.site.register(Proveedor)
admin.site.register(Comprador)
admin.site.register(Factura)
admin.site.register(Vacunas)
admin.site.register(Cirugias)
admin.site.register(Enfermedades)
admin.site.register(Otros)
admin.site.register(Account)