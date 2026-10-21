from django.test import TestCase
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto


class ProductoFormTests(TestCase):
    def datos(self, **cambios):
        datos = {
            "nombre": "Teclado mecánico",
            "descripcion": "Ejemplo ficticio",
            "precio": "15990.00",
            "cantidad": "50",
            "categoria": "perifericos",
        }
        datos.update(cambios)
        return datos

    def test_cantidad_valida(self):
        self.assertTrue(ProductoForm(data=self.datos(cantidad="50")).is_valid())

    def test_cantidad_negativa(self):
        self.assertFalse(ProductoForm(data=self.datos(cantidad="-1")).is_valid())

    def test_cantidad_limite_superior(self):
        self.assertTrue(ProductoForm(data=self.datos(cantidad="10000")).is_valid())

    def test_nombre_valido(self):
        self.assertTrue(ProductoForm(data=self.datos(nombre="Mouse")).is_valid())

    def test_nombre_demasiado_corto(self):
        self.assertFalse(ProductoForm(data=self.datos(nombre="AB")).is_valid())

    def test_nombre_limite_100_caracteres(self):
        self.assertTrue(ProductoForm(data=self.datos(nombre="A" * 100)).is_valid())

    def test_creacion_invalida_no_guarda(self):
        respuesta = self.client.post(reverse("inventario:crear"), self.datos(cantidad="-1"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Producto.objects.count(), 0)

    def test_eliminacion_solo_post(self):
        producto = Producto.objects.create(nombre="Mouse", precio="8990.00", cantidad=2, categoria="perifericos")
        respuesta = self.client.get(reverse("inventario:eliminar", args=[producto.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(Producto.objects.filter(pk=producto.pk).exists())
