from django.db import models

class ServicioEstetica(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_minutos = models.IntegerField()
    categoria_servicio = models.CharField(max_length=50)
    productos_usados = models.TextField()
    requiere_cita_previa = models.BooleanField()

    class Meta:
        db_table = 'servicio_estetica'

class ProfesionalEstetica(models.Model):
    id_profesional = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    horario_trabajo = models.TextField()

    class Meta:
        db_table = 'profesional_estetica'

class ClienteEstetica(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    preferencias_servicio = models.TextField()
    fecha_nacimiento = models.DateField()
    historial_alergias = models.TextField()

    class Meta:
        db_table = 'cliente_estetica'

class CitaEstetica(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('ClienteEstetica', on_delete=models.CASCADE)
    id_profesional = models.ForeignKey('ProfesionalEstetica', on_delete=models.CASCADE)
    id_servicio = models.ForeignKey('ServicioEstetica', on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado_cita = models.CharField(max_length=50)
    comentarios_cliente = models.TextField()
    precio_final_cita = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_real_minutos = models.IntegerField()

    class Meta:
        db_table = 'cita_estetica'

class ProductoVenta(models.Model):
    id_producto_venta = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_proveedor = models.IntegerField()
    marca = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    codigo_barra = models.CharField(max_length=50)

    class Meta:
        db_table = 'producto_venta'

class VentaProducto(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('ClienteEstetica', on_delete=models.CASCADE)
    id_profesional = models.ForeignKey('ProfesionalEstetica', on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    numero_factura = models.CharField(max_length=50)
    estado_venta = models.CharField(max_length=50)

    class Meta:
        db_table = 'venta_producto'

class DetalleVentaProducto(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('VentaProducto', on_delete=models.CASCADE)
    id_producto_venta = models.ForeignKey('ProductoVenta', on_delete=models.CASCADE)
    id_cita_asociada = models.ForeignKey('CitaEstetica', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_venta = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva_aplicado = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'detalle_venta_producto'
