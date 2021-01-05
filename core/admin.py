from django.contrib import admin
from core.models import Cliente, Producto, Venta, TipoPersona,TipoVenta,Categoria

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("name","last_name","cedula","tipo_persona")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(TipoPersona)
admin.site.register(TipoVenta)
admin.site.register(Categoria)

