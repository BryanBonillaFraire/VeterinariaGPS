from django.shortcuts import render, redirect
from .models import Propietario, Mascota, PagoServicio, Cita, Producto, PagoProducto, Proveedor, Comprador, Factura, Cirugias, Enfermedades, Otros, Vacunas
from .forms import PropietarioForm, MascotaForm, PagoServicioForm, CitaForm, ProductoForm, PagoProductoForm, ProveedorForm, CompradorForm, FacturaForm, CirugiasForm, EnfermedadesForm, OtrosForm, VacunasForm
from django.views.generic import (UpdateView)

# Create your views here.

def login(request):
    return render(request, 'ControlDeVeterinaria/log.html', {})

def index(request):
    return render(request, 'ControlDeVeterinaria/index.html', {})

def verMascota(request):
    listaMascotas = Mascota.objects.all()

    context ={
        'listaMascotas':listaMascotas
    }
    return render(request, 'ControlDeVeterinaria/mascota.html', context)

def crearMascota(request):
    form = MascotaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/mascota/')    
    context ={
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/crearMascota.html', context)

def borrarMascota(request,id):
    Mascota.objects.get(id=id).delete()

    return redirect('/mascota/')

def crearPropietario(request):
    listaPropietario = Propietario.objects.all()
    form = PropietarioForm(request.POST)
    if form.is_valid():
        form.save()
    context ={
        'form':form,
        'listaPropietario':listaPropietario
    }
    return render(request, 'ControlDeVeterinaria/crearPropietario.html', context)

def borrarPropietario(request,id):
    Propietario.objects.get(id=id).delete()

    return redirect('/propietario/')

def expediente(request):
    formCirugias = CirugiasForm(request.POST)
    formVacunas = VacunasForm(request.POST)
    formEnfermedades = EnfermedadesForm(request.POST)
    formOtros = OtrosForm(request.POST)
    if formCirugias.is_valid():
        formCirugias.save()
    if formVacunas.is_valid():
        formVacunas.save()
    if formEnfermedades.is_valid():
        formEnfermedades.save()
    if formOtros.is_valid():
        formOtros.save()
    context = {
        "formCirugias":formCirugias,
        "formVacunas":formVacunas,
        "formEnfermedades":formEnfermedades,
        "formOtros":formOtros,
    }
    return render(request, 'ControlDeVeterinaria/expediente.html', context)

def expediente_mascota(request, id):
    cirugias = Cirugias.objects.filter(mascota__id=id)
    vacunas = Vacunas.objects.filter(mascota__id=id)
    enfermedades = Enfermedades.objects.filter(mascota__id=id)
    otros = Otros.objects.filter(mascota__id=id)

    mascota = Mascota.objects.get(id=id)

    context ={
        'cirugias':cirugias,
        'vacunas':vacunas,
        'enfermedades':enfermedades,
        'otros':otros,
        'mascota':mascota,
    }
    return render(request, 'ControlDeVeterinaria/expediente-mascota.html', context)

def crearCita(request):
    form = CitaForm(request.POST)
    listaCitas = Cita.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaCitas':listaCitas,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/citas.html', context)

def borrarCita(request,id):
    Cita.objects.get(id=id).delete()
    return redirect('/citas/')

def pagoServicio(request):
    form = PagoServicioForm(request.POST)
    listaPagos = PagoServicio.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaPagos':listaPagos,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/pagos.html', context)

def borrarPago(request,id):
    PagoServicio.objects.get(id=id).delete()
    return redirect('/pagos/')

def producto(request):
    form = ProductoForm(request.POST)
    listaProductos = Producto.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaProductos':listaProductos,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/productos.html', context)

def borrarProducto(request,id):
    Producto.objects.get(id=id).delete()
    return redirect('/productos/')

def pagoProducto(request):
    form = PagoProductoForm(request.POST)
    listaPagoProductos = PagoProducto.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaPagoProductos':listaPagoProductos,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/pago_productos.html', context)

def borrarPagoProducto(request,id):
    PagoProducto.objects.get(id=id).delete()
    return redirect('/pago-productos/')

def factura(request):
    form = FacturaForm(request.POST)
    listaFactura = Factura.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaFactura':listaFactura,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/factura.html', context)

def borrarFactura(request,id):
    Factura.objects.get(id=id).delete()
    return redirect('/factura/')

def verFactura(request,id):
    datosFactura = Factura.objects.get(id=id)
    context = {
        'datosFactura':datosFactura,
    }
    return render(request, 'ControlDeVeterinaria/ver_factura.html', context)

def proveedor(request):
    form = ProveedorForm(request.POST)
    listaProveedor = Proveedor.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaProveedor':listaProveedor,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/proveedor.html', context)

def borrarProveedor(request,id):
    Proveedor.objects.get(id=id).delete()
    return redirect('/proveedor/')

def verProveedor(request,id):
    datosProveedor = Proveedor.objects.get(id=id)
    context = {
        'datosProveedor':datosProveedor,
    }
    return render(request, 'ControlDeVeterinaria/ver_proveedor.html', context)

def comprador(request):
    form = CompradorForm(request.POST)
    listaComprador = Comprador.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaComprador':listaComprador,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/comprador.html', context)

def borrarComprador(request,id):
    Comprador.objects.get(id=id).delete()
    return redirect('/comprador/')

def verComprador(request,id):
    datosComprador = Comprador.objects.get(id=id)
    context = {
        'datosComprador':datosComprador,
    }
    return render(request, 'ControlDeVeterinaria/ver_comprador.html', context)
