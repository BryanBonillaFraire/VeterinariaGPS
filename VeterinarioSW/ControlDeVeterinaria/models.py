from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, password):

        if not username:
            raise ValueError("Usuarios necesitan un nombre de usuario")
        if not password:
            raise ValueError("Usuarios necesitan una contraseña")

        user = self.model(
            username = username,
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,rol):

        user = self.create_user(
            password=password,
            username=username,
        )
        user.rol = 'ADMIN'
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    ROLES = (
        ('ADMIN','ADMIN'),
        ('EMPLEADO','EMPLEADO'),
    )
    rol = models.CharField(max_length=30, choices=ROLES)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol','password']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.rol=='ADMIN'

    def has_module_perms(self, app_label):
        return True

class Propietario(models.Model):
    nombrePropietario = models.CharField(max_length=30)
    telefonoMovil = models.CharField(max_length=10)
    telefonoCasa = models.CharField(max_length=10)
    correoElectronico = models.CharField(max_length=50)

    def __str__(self):
        return '%s - %s' % (self.id, self.nombrePropietario)

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.nombreMascota)

class PagoServicio(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)
    servicios = models.CharField(max_length=30)
    costoUnitario = models.IntegerField()
    montoTotal = models.IntegerField()
    montoPagado = models.IntegerField()
    formaPago = models.CharField(max_length=20)

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)
    fecha = models.DateTimeField(null=True, blank=True)
    motivo = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    especificaciones = models.CharField(max_length=20)
    costoUnitario = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.nombre, self.marca)

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
    
    def __str__(self):
        return '%s - %s' % (self.id, self.nombre)

class Comprador(models.Model):
    nombre = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    domicilio = models.CharField(max_length=50)
    cp = models.IntegerField()
    poblacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return '%s - %s' % (self.id, self.nombre)

class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True)
    comprador = models.ForeignKey(Comprador, on_delete=models.SET_NULL, null = True)
    numeroSerie = models.CharField(max_length=20)
    fechaExpedicion = models.DateField()
    concepto = models.CharField(max_length=10)
    costoUnitario = models.IntegerField()
    montoTotal = models.IntegerField()
    tipoImposito = models.IntegerField()

class Vacunas(models.Model):
    vacuna = models.CharField(max_length=30)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)

class Cirugias(models.Model):
    cirugia = models.CharField(max_length=30)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)

class Enfermedades(models.Model):
    enfermedad = models.CharField(max_length=30)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)

class Otros(models.Model):
    otro = models.CharField(max_length=30)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null = True)
