from django.db import models
from django.urls import reverse
import uuid

class Aroma(models.Model):
    nombre = models.CharField(
    max_length=20,
    )
    
    descripcion = models.TextField(max_length=2000, default= "Descripción del aroma")

    class Meta:
        ordering = ['nombre']

    def get_absolute_url(self):
	    return reverse('aroma_detail', args=[str(self.id)])
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    aroma = models.ForeignKey('Aroma',on_delete=models.SET_NULL, null=True, blank=False)
    TIPO_PROD = (
        ('Tripack','Tripack'),
        ('Bótox','Bótox'),
        ('Spray Termoprotector','Spray Termoprotector'),
    )

    descripcion_prod = models.TextField(max_length=2000, default= "Descripción del producto")

    tipo_producto = models.CharField(
        max_length=20,
        choices= TIPO_PROD,
        default='Tripack',
        )

    precio = models.IntegerField(default=0)
        
    class Meta:
        ordering = ['tipo_producto']
    
    def get_absolute_url(self):
        return reverse('producto_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.tipo_producto}'
    