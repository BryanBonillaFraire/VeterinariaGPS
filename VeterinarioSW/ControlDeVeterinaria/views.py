from django.shortcuts import render, redirect
from .models import Propietario, Mascota, PagoServicio, Cita, Producto, PagoProducto, Proveedor, Comprador, Factura, Cirugias, Enfermedades, Otros, Vacunas, Account
from .forms import PropietarioForm, MascotaForm, PagoServicioForm, CitaForm, ProductoForm, PagoProductoForm, ProveedorForm, CompradorForm, FacturaForm, CirugiasForm, EnfermedadesForm, OtrosForm, VacunasForm,AccountForm
from django.views.generic import (UpdateView)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from datetime import date

from django.contrib.auth.decorators import login_required

# Create your views here.

def loginUser(request):

    if request.method == "POST":
        usernameCompare = request.POST.get('username')
        passwordCompare = request.POST.get('password')
        usuarioEncontrado = False
        usuario = ""

        User = get_user_model()
        users = User.objects.all()
        for user in users:
            if user.username == usernameCompare and user.password == passwordCompare:
                usuarioEncontrado = True
                usuario = user
        
        if usuarioEncontrado:
            login(request, usuario)
            return render(request, 'ControlDeVeterinaria/index.html')     
        else:
            messages.info(request, 'Nombre de usuario o contraseña erroneo')
    return render(request, 'ControlDeVeterinaria/log.html', {})

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def index(request):
    return render(request, 'ControlDeVeterinaria/index.html', {})

def calendario(request, mes=1):
    dateHoy=date.today()
    print(mes)
    return render(request, 'ControlDeVeterinaria/calendario.html', {})

@login_required(login_url='login')
def verMascota(request):
    listaMascotas = Mascota.objects.all()

    context ={
        'listaMascotas':listaMascotas
    }
    return render(request, 'ControlDeVeterinaria/mascota.html', context)

@login_required(login_url='login')
def crearMascota(request):
    form = MascotaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/mascota/')    
    context ={
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/crearMascota.html', context)

@login_required(login_url='login')
def borrarMascota(request,id):
    Mascota.objects.get(id=id).delete()

    return redirect('/mascota/')

@login_required(login_url='login')
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

@login_required(login_url='login')
def borrarPropietario(request,id):
    Propietario.objects.get(id=id).delete()

    return redirect('/propietario/')

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def borrarCita(request,id):
    Cita.objects.get(id=id).delete()
    return redirect('/citas/')

@login_required(login_url='login')
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

@login_required(login_url='login')
def borrarPago(request,id):
    PagoServicio.objects.get(id=id).delete()
    return redirect('/pagos/')

@login_required(login_url='login')
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

@login_required(login_url='login')
def borrarProducto(request,id):
    Producto.objects.get(id=id).delete()
    return redirect('/productos/')

@login_required(login_url='login')
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

@login_required(login_url='login')
def borrarPagoProducto(request,id):
    PagoProducto.objects.get(id=id).delete()
    return redirect('/pago-productos/')

@login_required(login_url='login')
def factura(request):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    form = FacturaForm(request.POST)
    listaFactura = Factura.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaFactura':listaFactura,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/factura.html', context)

@login_required(login_url='login')
def borrarFactura(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    Factura.objects.get(id=id).delete()
    return redirect('/factura/')

@login_required(login_url='login')
def verFactura(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    datosFactura = Factura.objects.get(id=id)
    context = {
        'datosFactura':datosFactura,
    }
    return render(request, 'ControlDeVeterinaria/ver_factura.html', context)

@login_required(login_url='login')
def proveedor(request):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    form = ProveedorForm(request.POST)
    listaProveedor = Proveedor.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaProveedor':listaProveedor,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/proveedor.html', context)

@login_required(login_url='login')
def borrarProveedor(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    Proveedor.objects.get(id=id).delete()
    return redirect('/proveedor/')

@login_required(login_url='login')
def verProveedor(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    datosProveedor = Proveedor.objects.get(id=id)
    context = {
        'datosProveedor':datosProveedor,
    }
    return render(request, 'ControlDeVeterinaria/ver_proveedor.html', context)

@login_required(login_url='login')
def comprador(request):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    form = CompradorForm(request.POST)
    listaComprador = Comprador.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaComprador':listaComprador,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/comprador.html', context)

@login_required(login_url='login')
def borrarComprador(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    Comprador.objects.get(id=id).delete()
    return redirect('/comprador/')

@login_required(login_url='login')
def verComprador(request,id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    datosComprador = Comprador.objects.get(id=id)
    context = {
        'datosComprador':datosComprador,
    }
    return render(request, 'ControlDeVeterinaria/ver_comprador.html', context)

@login_required(login_url='login')
def crearAccount(request):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    form = AccountForm(request.POST)
    listaAccounts = Account.objects.all()
    if form.is_valid():
        form.save()    
    context ={
        'listaAccounts':listaAccounts,
        'form':form,
    }
    return render(request, 'ControlDeVeterinaria/accounts.html', context)

@login_required(login_url='login')
def borrarAccount(request, id):
    rol = request.user.rol
    if rol == 'EMPLEADO':
        return redirect('/index/')
    Account.objects.get(id=id).delete()
    return redirect('/accounts/')