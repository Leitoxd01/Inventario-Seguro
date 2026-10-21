from decimal import Decimal

from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models


class Producto(models.Model):
    class Categoria(models.TextChoices):
        COMPUTACION = "computacion", "Computación"
        PERIFERICOS = "perifericos", "Periféricos"
        COMPONENTES = "componentes", "Componentes"
        OTROS = "otros", "Otros"

    nombre = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
