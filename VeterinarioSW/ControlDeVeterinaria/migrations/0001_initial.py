# Generated by Django 3.1 on 2020-11-20 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rfc', models.CharField(max_length=13)),
                ('domicilio', models.CharField(max_length=50)),
                ('cp', models.IntegerField()),
                ('poblacion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('especificaciones', models.CharField(max_length=20)),
                ('costoUnitario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePropietario', models.CharField(max_length=30)),
                ('telefonoMovil', models.CharField(max_length=10)),
                ('telefonoCasa', models.CharField(max_length=10)),
                ('correoElectronico', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rfc', models.CharField(max_length=13)),
                ('domicilio', models.CharField(max_length=50)),
                ('cp', models.IntegerField()),
                ('poblacion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PagoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicios', models.CharField(max_length=30)),
                ('costoUnitario', models.IntegerField()),
                ('montoTotal', models.IntegerField()),
                ('montoPagado', models.IntegerField()),
                ('formaPago', models.CharField(max_length=20)),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='PagoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montoTotal', models.IntegerField()),
                ('formaPago', models.CharField(max_length=20)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=20)),
                ('especie', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroSerie', models.CharField(max_length=20)),
                ('fechaExpedicion', models.DateField()),
                ('concepto', models.CharField(max_length=10)),
                ('costoUnitario', models.IntegerField()),
                ('montoTotal', models.IntegerField()),
                ('tipoImposito', models.IntegerField()),
                ('comprador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.comprador')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cirugias', models.TextField()),
                ('vacunas', models.TextField()),
                ('enfermedades', models.TextField()),
                ('otros', models.TextField()),
                ('mascota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('mascota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ControlDeVeterinaria.mascota')),
            ],
        ),
    ]