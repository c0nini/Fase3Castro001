from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('aromas', views.AromaListView.as_view(), name='aromas'),
    path('contacto', views.contacto, name='contacto'),
    path('aroma/<int:pk>', views.AromaDetailView.as_view(), name='aroma_detail'),
    path('producto/<str:pk>', views.ProductoDetailView.as_view(), name='producto_detail'),
]

urlpatterns += [
    path('producto/create/', views.producto_new, name='producto_create'),
    path('producto/<str:pk>/update/', views.producto_edit, name='producto_update'),
    path('producto/<str:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
    path('aroma/create/', views.aroma_new, name='aroma_create'),
    path('aroma/<int:pk>/update/', views.aroma_edit, name='aroma_update'),
    path('aroma/<int:pk>/delete/', views.AromaDelete.as_view(), name='aroma_delete'),

]