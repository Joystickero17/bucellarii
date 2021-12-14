"""aerarium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import core.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Async Views
    path("async/products", views.ProductsAsyncView.as_view(), name="async_products"),
    path("async/clients", views.ClientsAsyncView.as_view(), name="async_clients"),
    path('admin/', admin.site.urls),
    path("", views.InicioEsp.as_view(), name="index"),
    path("productos", views.ProductView.as_view(), name="productos"),
    path("productos/<int:page>", views.ProductView.as_view(), name="productos"),
    path("productos/insert", views.ProductEditView.as_view(), name="productos_insert"),
    path("productos/<int:page>", views.ProductView.as_view(), name="productos_delete"),
    path("productos/update/<int:pk>", views.ProductosUpdate.as_view(), name="productos_update"),
    path("productos/del/<int:pk>", views.ProductoDeleteView.as_view(), name="borrar_productos"),
    path("clientes", views.ClientesView.as_view(), name="clientes"),
    path("clientes/insert", views.ClienteEditView.as_view(), name="clientes_insert"),
    path("clientes/<int:page>", views.ClientesView.as_view(), name="clientes"),
    path("clientes/update/<int:pk>", views.ClientesUpdate.as_view(), name="clientes_update"),
    path("clientes/del/<int:pk>", views.ClienteDeleteView.as_view(), name="clientes_delete"),
    path("ventas", views.VentasView.as_view(), name="ventas"),
    path("ventas/insert", views.VentaEditView.as_view(), name="ventas_insert"),
    path("ventas/<int:page>", views.VentasView.as_view(), name="ventas"),
    path("ventas/update/<int:pk>", views.VentasUpdate.as_view(), name="ventas_update"),
    path("categorias", views.CategoriaView.as_view(), name="categorias"),
    path("categorias/insert", views.CategoriaEditView.as_view(), name="categorias_insert"),
    path("categorias/update/<int:pk>", views.CategoriasUpdate.as_view(), name="categorias_update"),
    path("test", views.checkout, name="prueba")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
