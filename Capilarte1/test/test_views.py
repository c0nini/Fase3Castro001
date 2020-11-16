from django.test import TestCase
from django.urls import reverse
from Capilarte1.models import Aroma, Producto

class AromaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_aroma = 8

        for aroma_id in range(number_of_aroma):
            Aroma.objects.create(
                nombre=f'Jalea Real {aroma_id}',
                descripcion=f'Prueba {aroma_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/aromas')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('aromas'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('aromas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Capilarte1/aroma_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('aromas'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['aroma_list']) == 5)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('aromas')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['aroma_list']) == 3)

class MovieListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_producto = 13
        a =Aroma.objects.create(nombre='Jalea Real', descripcion='Prueba')

        for producto_id in range(number_of_producto):
            test_producto = Producto.objects.create(
                tipo_producto=f'Tripack {producto_id}',
                descripcion_prod=f'Prueba {producto_id}',
                aroma= a,
                precio=10000 
            )
            
            test_producto.save()
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/productos')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'productos.html')