from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin, UpdateView, CreateView
from core.models import Producto, Cliente, Venta, Categoria
from .forms import ProductoForm, ClienteForm, VentaForm, CategoryForm
from django.http import JsonResponse

# Create your views here.
APPNAME = "core"

class JsonGeneralView(View):
    model = None
    def get(self, *args, **kwargs):
        if "keyword" not in self.request.GET.keys():
            model_list = list(self.model.objects.all().values())
        else:
            model_list = list(self.model.objects.filter(name__contains=self.request.GET["keyword"]).values())
        print(model_list)
        return JsonResponse({"object_list":model_list})

class ClientsAsyncView(JsonGeneralView):
    model = Cliente

class ProductsAsyncView(JsonGeneralView):
    model = Producto
        

class Base(View):
    title = "Undefined"

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.context_dict = {"title": self.title}

    def get(self, request):
        pass


class BaseModelData():
    url_name = None
    model = None
    form_class = None
    def __init__(self, *args, **kwargs):
        if not self.url_name:
            raise ValueError("url_name must have something :(")
        if not self.model: 
            raise ValueError("model must be specified :(")
        if not self.form_class:
            print(f"WARNING Form_class not defined in {self.url_name}Data class!!!")

# clases con los datos básicos.
class ProductosData(BaseModelData):
    model = Producto
    form_class = ProductoForm
    url_name = "productos"


class ClienteData(BaseModelData):
    model = Cliente
    form_class = ClienteForm
    url_name = "clientes"


class VentaData(BaseModelData):
    model = Venta
    form_class = VentaForm
    url_name = "ventas"


class CategoriaData(BaseModelData):
    model = Categoria
    form_class = CategoryForm
    url_name = "categorias"


class DeleteEntity(View):
    # clase para borrar un elemento en la BBDD
    model = None
    redirect_to = 'index'

    def get(self, request, pk):
        object_to_delete = self.model.objects.get(pk=self.kwargs["pk"])
        object_to_delete.delete()
        return redirect(reverse(self.redirect_to, kwargs={"page": 1})+"?delete")


class ExtendedListView(ListView, BaseModelData):
    # clase con funciones extendidas de ListView

    theaders = None
    url_name = None
    template_name = None

    def __init__(self, *args, **kwargs):
        
        super().__init__()
        if not self.theaders:
            raise NameError("theaders is empty")
        if not self.url_name:
            raise NameError(
                "must specify url name to render in pagination template")

        self.template_name = APPNAME + "/" + self.url_name + "_body_list.html"

    def get(self, request, page=1, delete=0, update=0, **kwargs):
        super().get(request)
        context = super().get_context_data(**kwargs)
        context["total_pages"] = range(1, context["paginator"].num_pages+1)
        context["theaders"] = ["ID"]
        context["theaders"] += self.theaders
        context["url_name"] = self.url_name
        print(self.url_name)
        print(self.template_name)
        return render(request, self.template_name, context)


# Create Views - Vistas de Inserción
class ProductEditView(ProductosData, CreateView):
    success_url = "/productos?added"


class ClienteEditView(ClienteData, CreateView):
    success_url = "/clientes?added"


class CategoriaEditView(CategoriaData, CreateView):
    success_url = "/categorias?added"


class VentaEditView(VentaData, CreateView):
    success_url = "/ventas?added"

def checkout(request):
    product_list = Producto.objects.all()
    return render(request, "core/test.html", {"product_list": product_list})


# Extended List View - Vistas que Despliegan una lista del entidades del modelo
class ClientesView(ClienteData, ExtendedListView):
    paginate_by = 10
    theaders = ["Nombres", "Apellidos", "Cédula", "tipo de Persona"]


class VentasView(VentaData, ExtendedListView):
    paginate_by = 10
    theaders = ["Cliente", "Total de la venta",
                "Tipo de Pago", "IVA", "Excento"]


class CategoriaView(CategoriaData, ExtendedListView):
    paginate_by = 10
    theaders = ["Categoría Padre","Categoría"]


class ProductView(ProductosData, ExtendedListView):
    paginate_by = 10
    theaders = ["producto", "categoría","IVA", "Precio Neto", "Precio + Iva"]

# UpdateViews - Vistas para actualizar entidades seleccionadas
class ClientesUpdate(ClienteData, UpdateView):
    success_url = "/clientes?updated"


class ProductosUpdate(ProductosData, UpdateView):
    success_url = "/productos?updated"


class CategoriasUpdate(CategoriaData, UpdateView):
    success_url = "/categorias?updated"


class VentasUpdate(VentaData, UpdateView):
    success_url = "/ventas?updated"

# DeleteEntityViews - Vistas de Eliminación de entidades
class ClienteDeleteView(DeleteEntity):
    model = Producto
    redirect_to = "clientes"


class VentaDeleteView(DeleteEntity):
    model = Producto
    redirect_to = "ventas"


class ProductoDeleteView(DeleteEntity):
    model = Producto
    redirect_to = "productos"


class InicioEsp(Base):
    title = "Inicio"

    def get(self, request):
        super().get(request)
        self.context_dict["q_clientes"] = Cliente.objects.count
        return render(request, "core/inicio.html", self.context_dict)
