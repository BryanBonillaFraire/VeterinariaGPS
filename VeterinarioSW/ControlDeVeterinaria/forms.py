from django import forms
from .models import Mascota, Propietario, PagoServicio, Cita, Expediente, Producto, PagoProducto, Proveedor, Comprador, Factura


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombreMascota', 'especie', 'raza', 'edad', 'propietario']

    def __init__(self, *args, **kwargs):
        super(MascotaForm).__init__(*args, **kwargs)
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
        super(PropietarioForm).__init__(*args, **kwargs)
        self.fields['nombrePropietario'].widget.attrs['class'] = 'form-control'
        self.fields['telefonoMovil'].widget.attrs['class'] = 'form-control'
        self.fields['telefonoCasa'].widget.attrs['class'] = 'form-control'
        self.fields['correoElectronico'].widget.attrs['class'] = 'form-control'

class PagoServicioForm(forms.ModelForm):
    class Meta:
        model = PagoServicio
        fields = ['propietario', 'servicios', 'costoUnitario', 'montoTotal','montoPagado','formaPago']

    def __init__(self, *args, **kwargs):
        super(PagoServicioForm).__init__(*args, **kwargs)
        self.fields['propietario'].widget.attrs['class'] = 'form-control'
        self.fields['servicios'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['formaPago'].widget.attrs['class'] = 'form-control'
        self.fields['montoPagado'].widget.attrs['class'] = 'form-control'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'motivo']

    def __init__(self, *args, **kwargs):
        super(CitaForm).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['motivo'].widget.attrs['class'] = 'form-control'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'marca', 'especificaciones','costoUnitario']

    def __init__(self, *args, **kwargs):
        super(ProductoForm).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        self.fields['marca'].widget.attrs['class'] = 'form-control'
        self.fields['especificaciones'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['mascota', 'cirugias', 'vacunas', 'enfermedades','otros']

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm).__init__(*args, **kwargs)
        self.fields['mascota'].widget.attrs['class'] = 'form-control'
        self.fields['cirugias'].widget.attrs['class'] = 'form-control'
        self.fields['vacunas'].widget.attrs['class'] = 'form-control'
        self.fields['enfermedades'].widget.attrs['class'] = 'form-control'
        self.fields['otros'].widget.attrs['class'] = 'form-control'

class PagoProductoForm(forms.ModelForm):
    class Meta:
        model = PagoProducto
        fields = ['producto', 'montoTotal', 'formaPago']

    def __init__(self, *args, **kwargs):
        super(PagoProductoForm).__init__(*args, **kwargs)
        self.fields['producto'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['formaPago'].widget.attrs['class'] = 'form-control'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'rfc', 'domicilio','cp','poblacion','telefono','correo']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm).__init__(*args, **kwargs)
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
        super(CompradorForm).__init__(*args, **kwargs)
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
        super(FacturaForm).__init__(*args, **kwargs)
        self.fields['proveedor'].widget.attrs['class'] = 'form-control'
        self.fields['comprador'].widget.attrs['class'] = 'form-control'
        self.fields['numeroSerie'].widget.attrs['class'] = 'form-control'
        self.fields['fechaExpedicion'].widget.attrs['class'] = 'form-control'
        self.fields['concepto'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'
        self.fields['montoTotal'].widget.attrs['class'] = 'form-control'
        self.fields['tipoImposito'].widget.attrs['class'] = 'form-control'

