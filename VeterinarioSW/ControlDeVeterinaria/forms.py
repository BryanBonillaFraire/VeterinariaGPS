from django import forms
from .models import Mascota, Propietario, PagoServicio, Cita, Producto, PagoProducto, Proveedor, Comprador, Factura, Cirugias, Vacunas, Otros, Enfermedades, Account


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombreMascota', 'especie', 'raza', 'edad', 'propietario']

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['nombreMascota'].widget.attrs['class'] = 'form-control'
        self.fields['especie'].widget.attrs['class'] = 'form-control'
        self.fields['raza'].widget.attrs['class'] = 'form-control'
        self.fields['edad'].widget.attrs['class'] = 'form-control'
        self.fields['propietario'].widget.attrs['class'] = 'form-control'

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombrePropietario', 'telefonoMovil', 'telefonoCasa', 'correoElectronico']

    def __init__(self, *args, **kwargs):
        super(PropietarioForm, self).__init__(*args, **kwargs)
        self.fields['nombrePropietario'].widget.attrs['class'] = 'form-control'
        self.fields['telefonoMovil'].widget.attrs['class'] = 'form-control'
        self.fields['telefonoCasa'].widget.attrs['class'] = 'form-control'
        self.fields['correoElectronico'].widget.attrs['class'] = 'form-control'

class PagoServicioForm(forms.ModelForm):
    class Meta:
        model = PagoServicio
        fields = ['propietario', 'servicios', 'costoUnitario', 'montoTotal','montoPagado','formaPago']

    def __init__(self, *args, **kwargs):
        super(PagoServicioForm, self).__init__(*args, **kwargs)
        self.fields['propietario'].widget.attrs['class'] = 'form-control'
        self.fields['servicios'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['formaPago'].widget.attrs['class'] = 'form-control'
        self.fields['montoPagado'].widget.attrs['class'] = 'form-control'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'motivo', 'fecha']

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['motivo'].widget.attrs['class'] = 'form-control'
        self.fields['fecha'].widget.attrs['placeholder'] = 'EJ. 2020-11-02 7:00:00'
        self.fields['fecha'].widget.attrs['class'] = 'form-control'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'marca', 'especificaciones','costoUnitario']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        self.fields['marca'].widget.attrs['class'] = 'form-control'
        self.fields['especificaciones'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'

class CirugiasForm(forms.ModelForm):
    class Meta:
        model = Cirugias
        fields = ['mascota', 'cirugia']

    def __init__(self, *args, **kwargs):
        super(CirugiasForm, self).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['cirugia'].widget.attrs['class'] = 'form-control'

class VacunasForm(forms.ModelForm):
    class Meta:
        model = Vacunas
        fields = ['mascota', 'vacuna']

    def __init__(self, *args, **kwargs):
        super(VacunasForm, self).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['vacuna'].widget.attrs['class'] = 'form-control'

class EnfermedadesForm(forms.ModelForm):
    class Meta:
        model = Enfermedades
        fields = ['mascota', 'enfermedad']

    def __init__(self, *args, **kwargs):
        super(EnfermedadesForm, self).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['enfermedad'].widget.attrs['class'] = 'form-control'

class OtrosForm(forms.ModelForm):
    class Meta:
        model = Otros
        fields = ['mascota', 'otro']

    def __init__(self, *args, **kwargs):
        super(OtrosForm, self).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['otro'].widget.attrs['class'] = 'form-control'

class PagoProductoForm(forms.ModelForm):
    class Meta:
        model = PagoProducto
        fields = ['producto', 'montoTotal', 'formaPago']

    def __init__(self, *args, **kwargs):
        super(PagoProductoForm, self).__init__(*args, **kwargs)
        self.fields['producto'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['formaPago'].widget.attrs['class'] = 'form-control'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'rfc', 'domicilio','cp','poblacion','telefono','correo']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['rfc'].widget.attrs['class'] = 'form-control'
        self.fields['domicilio'].widget.attrs['class'] = 'form-control'
        self.fields['cp'].widget.attrs['class'] = 'form-control'
        self.fields['poblacion'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['correo'].widget.attrs['class'] = 'form-control'

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['nombre', 'rfc', 'domicilio','cp','poblacion','telefono','correo']

    def __init__(self, *args, **kwargs):
        super(CompradorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['rfc'].widget.attrs['class'] = 'form-control'
        self.fields['domicilio'].widget.attrs['class'] = 'form-control'
        self.fields['cp'].widget.attrs['class'] = 'form-control'
        self.fields['poblacion'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['correo'].widget.attrs['class'] = 'form-control'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['proveedor', 'comprador', 'numeroSerie','fechaExpedicion','concepto','costoUnitario','montoTotal','tipoImposito']

    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].widget.attrs['class'] = 'form-control'
        self.fields['comprador'].widget.attrs['class'] = 'form-control'
        self.fields['numeroSerie'].widget.attrs['class'] = 'form-control'
        self.fields['fechaExpedicion'].widget.attrs['placeholder'] = 'EJ. 2020-11-02'
        self.fields['fechaExpedicion'].widget.attrs['class'] = 'form-control'
        self.fields['concepto'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['tipoImposito'].widget.attrs['class'] = 'form-control'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'rol']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['rol'].widget.attrs['class'] = 'form-control'

