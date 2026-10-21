from django.urls import path

from . import views

app_name = "inventario"

urlpatterns = [
    path("", views.producto_lista, name="lista"),
    path("producto/nuevo/", views.producto_crear, name="crear"),
    path("producto/<int:pk>/", views.producto_detalle, name="detalle"),
    path("producto/<int:pk>/editar/", views.producto_editar, name="editar"),
    path("producto/<int:pk>/eliminar/", views.producto_eliminar, name="eliminar"),
]
