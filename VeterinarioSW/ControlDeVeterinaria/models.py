from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombrePropietario = models.CharField(max_length=30)
    telefonoMovil = models.CharField(max_length=10)
    telefonoCasa = models.CharField(max_length=10)
    correoElectronico = models.CharField(max_length=50)

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)

class PagoServicio(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)
    servicios = models.CharField(max_length=30)
    costoUnitario = models.IntegerField()
    montoTotal = models.IntegerField()
    montoPagado = models.IntegerField()
    formaPago = models.CharField(max_length=20)

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)
    motivo = models.TextField()

class Expediente(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)
    cirugias = models.TextField()
    vacunas = models.TextField()
    enfermedades = models.TextField()
    otros = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    especificaciones = models.CharField(max_length=20)
    costoUnitario = models.IntegerField()

class PagoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)
    montoTotal = models.IntegerField()
    formaPago = models.CharField(max_length=20)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    domicilio = models.CharField(max_length=50)
    cp = models.IntegerField()
    poblacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

class Comprador(models.Model):
    nombre = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    domicilio = models.CharField(max_length=50)
    cp = models.IntegerField()
    poblacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True)
    comprador = models.ForeignKey(Comprador, on_delete=models.SET_NULL, null = True)
    numeroSerie = models.CharField(max_length=20)
    fechaExpedicion = models.DateField()
    concepto = models.CharField(max_length=10)
    costoUnitario = models.IntegerField()
    montoTotal = models.IntegerField()
    tipoImposito = models.IntegerField()