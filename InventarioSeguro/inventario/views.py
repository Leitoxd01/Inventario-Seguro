from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, "inventario/producto_lista.html", {"productos": productos})


def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "inventario/producto_detalle.html", {"producto": producto})


def producto_crear(request):
    formulario = ProductoForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        messages.success(request, "Producto creado correctamente.")
        return redirect("inventario:lista")
    return render(request, "inventario/producto_formulario.html", {"formulario": formulario, "titulo": "Nuevo producto"})


def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    formulario = ProductoForm(request.POST or None, instance=producto)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        messages.success(request, "Producto actualizado correctamente.")
        return redirect("inventario:lista")
    return render(request, "inventario/producto_formulario.html", {"formulario": formulario, "titulo": "Editar producto"})


def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect("inventario:lista")
    return render(request, "inventario/producto_confirmar_eliminar.html", {"producto": producto})
