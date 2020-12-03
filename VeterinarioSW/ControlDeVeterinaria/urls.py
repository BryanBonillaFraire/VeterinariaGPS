from django.urls import path
from .views import loginUser, index, crearMascota, borrarMascota,calendario
from .views import crearPropietario, borrarPropietario, verMascota
from .views import expediente, expediente_mascota, crearCita, borrarCita, pagoServicio, borrarPago
from .views import producto, borrarProducto, pagoProducto, borrarPagoProducto
from .views import factura, proveedor, comprador, borrarFactura, borrarProveedor, borrarComprador
from .views import verComprador, verFactura, verProveedor, crearAccount, borrarAccount, logoutUser

urlpatterns = [
    path('', loginUser, name="login"),
    path('index/', index, name="index"),
    path('mascota/', verMascota, name="ver-mascota"),
    path('crear-mascota/', crearMascota, name="crear-mascota"),
    path('borrar-mascota/<int:id>', borrarMascota, name="borrar-mascota"),
    path('propietario/', crearPropietario, name="crear-propietario"),
    path('borrar-propietario/<int:id>', borrarPropietario, name="borrar-propietario"),
    path('expediente/', expediente, name="expediente"),
    path('expediente-mascota/<int:id>', expediente_mascota, name="expediente-mascota"),
    path('citas/', crearCita, name="crear-cita"),
    path('borrar-cita/<int:id>', borrarCita, name="borrar-cita"),
    path('pagos/', pagoServicio, name="pago-servicio"),
    path('borrar-pago/<int:id>', borrarPago, name="borrar-pago"),
    path('productos/', producto, name="productos"),
    path('borrar-productos/<int:id>', borrarProducto, name="borrar-producto"),
    path('pago-productos/', pagoProducto, name="pago-productos"),
    path('borrar-pago-productos/<int:id>', borrarPagoProducto, name="borrar-pago-producto"),
    path('factura/', factura, name="factura"),
    path('borrar-factura/<int:id>', borrarFactura, name="borrar-factura"),
    path('proveedor/', proveedor, name="proveedor"),
    path('borrar-proveedor/<int:id>', borrarProveedor, name="borrar-proveedor"),
    path('comprador/', comprador, name="comprador"),
    path('borrar-comprador/<int:id>', borrarComprador, name="borrar-comprador"),
    path('ver-comprador/<int:id>', verComprador, name="ver-comprador"),
    path('ver-proveedor/<int:id>', verProveedor, name="ver-proveedor"),
    path('ver-factura/<int:id>', verFactura, name="ver-factura"),
    path('accounts/', crearAccount, name="accounts"),
    path('borrar-account/<int:id>', borrarAccount, name="borrar-account"),
    path('logout/', logoutUser, name="logout"),
]