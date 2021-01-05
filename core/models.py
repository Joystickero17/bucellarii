from django.db import models

# Create your models here.

class TipoPersona(models.Model):
    name = models.CharField(max_length=1)
    class Meta:
        verbose_name = "Tipo de Persona"
        verbose_name_plural = "Tipo de Personas"
    def __str__(self):
        return self.name


class Cliente(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cedula = models.CharField(max_length=50, unique=True)
    tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.RESTRICT)
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.name + " "+ self.last_name


class Categoria(models.Model):
    father = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.get_full_route()

    def get_full_route(self):
        parent = self.father
        route = ""
        while True:
            if parent:
                route += parent.name + " → "
                parent = parent.father
            else:
                route += self.name
                break
        return route


class Producto(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(null=True)
    iva = models.IntegerField(default=0, blank=True)
    total = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total = self.price * (self.iva/100) + self.price

        return super().save(*args,**kwargs)

class TipoVenta(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Venta(models.Model):
    # Campos relacionales
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_venta = models.ForeignKey(TipoVenta, on_delete=models.RESTRICT)
    # Campos comunes
    fecha_anidado = models.DateTimeField(auto_now_add=True, null=True)
    total = models.FloatField()

    def __str__(self):
        return str(self.pk) + " - " + self.cliente.name +" - "+self.cliente.last_name

class VentaProductos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    venta = models.ForeignKey(Venta, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    fecha_anidado = models.DateTimeField(auto_now_add=True, null=True)