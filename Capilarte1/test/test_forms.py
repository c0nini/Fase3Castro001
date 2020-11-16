from django.test import TestCase
from Capilarte1.forms import AromaForm, ProductoForm
from Capilarte1.models import Aroma, Producto

class AromaFormsTest(TestCase):
    def test_valid_form(self):
        a = Aroma.objects.create(nombre='Prueba', descripcion='Prueba')
        data = {'nombre': a.nombre, 'descripcion': a.descripcion,}
        form = AromaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Aroma.objects.create(nombre='', descripcion='Prueba')
        data = {'nombre': a.nombre, 'descripcion': a.descripcion,}
        form = AromaForm(data=data)
        self.assertFalse(form.is_valid())

class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        aroma = Aroma.objects.create(nombre='1', descripcion='Prueba')
        aroma = Aroma.objects.get(pk=1).pk
        prod = Producto.objects.create(tipo_producto='Tripack', descripcion_prod='Prueba', precio=10000)
        prod.save()
        data = {'tipo_producto': prod.tipo_producto, 'descripcion_prod': prod.descripcion_prod, 'aroma': aroma, 'precio' : prod.precio, }
        form = ProductoForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Aroma.objects.create(nombre='Jalea Real', descripcion='Prueba')
        prod = Producto.objects.create(tipo_producto='', descripcion_prod='Prueba', aroma=a, precio=10000)
        data = {'tipo_producto': prod.tipo_producto, 'descripcion_prod': prod.descripcion_prod, 'aroma': prod.aroma, 'precio' : prod.precio, }
        form = ProductoForm(data=data)
        self.assertFalse(form.is_valid())