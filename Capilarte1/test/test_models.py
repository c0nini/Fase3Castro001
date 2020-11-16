from django.test import TestCase
from Capilarte1.models import Aroma, Producto

class AromaModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Aroma.objects.create(nombre='Jalea Real', descripcion='Prueba')
    
    def test_nombre_label(self):
        aroma=Aroma.objects.get(id=1)
        field_label = aroma._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_descripcion_label(self):
        aroma=Aroma.objects.get(id=1)
        field_label = aroma._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')
    
    def test_nombre_max_length(self):
        aroma=Aroma.objects.get(id=1)
        max_length = aroma._meta.get_field('nombre').max_length
        self.assertEquals(max_length,20)
    
    def test_descripcion_max_length(self):
        aroma=Aroma.objects.get(id=1)
        max_length = aroma._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,2000)
        
    def test_get_absolute_url(self):
        aroma=Aroma.objects.get(id=1)
        self.assertEquals(aroma.get_absolute_url(), '/aroma/1')

class ProductoModelTest(TestCase):

    @classmethod


    def setUpTestData(cls):
        ar = Aroma.objects.create(nombre="Jalea Real", descripcion='Prueba')
        test_producto = Producto.objects.create(id= '6d323a2e-e57f-4975-86f2-db23b8bb867d', tipo_producto="Tripack", descripcion_prod='Prueba', aroma=ar)
    
    def test_tipo_producto_label(self):
        
        producto= Producto.objects.get(id= '6d323a2e-e57f-4975-86f2-db23b8bb867d')
        field_label = producto._meta.get_field('tipo_producto').verbose_name
        self.assertEquals(field_label,'tipo producto')

    def test_descripcion_prod_label(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        field_label = producto._meta.get_field('descripcion_prod').verbose_name
        self.assertEquals(field_label,'descripcion prod')
    
    def test_aroma_label(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        field_label = producto._meta.get_field('aroma').verbose_name
        self.assertEquals(field_label,'aroma')

    def test_precio_label(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        field_label = producto._meta.get_field('precio').verbose_name
        self.assertEquals(field_label,'precio')
    
    def test_tipo_producto_max_length(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        max_length = producto._meta.get_field('tipo_producto').max_length
        self.assertEquals(max_length,20)
    
    def test_descripcion_prod_max_length(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        max_length = producto._meta.get_field('descripcion_prod').max_length
        self.assertEquals(max_length,2000)
        
    def test_get_absolute_url(self):
        producto=Producto.objects.get(id='6d323a2e-e57f-4975-86f2-db23b8bb867d')
        self.assertEquals(producto.get_absolute_url(), '/producto/6d323a2e-e57f-4975-86f2-db23b8bb867d')