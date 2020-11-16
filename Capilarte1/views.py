from django.shortcuts import render,redirect, get_object_or_404
from . models import Aroma, Producto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from . forms import AromaForm, ProductoForm

def index(request):
   
    return render(
        request,
        'index.html',
    )

def productos(request):
   
    return render(
        request,
        'productos.html',
    )

def contacto(request):
   
    return render(
        request,
        'contacto.html',
    )

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

class ProductoDetailView(generic.DetailView):
    model = Producto

class AromaDelete(DeleteView):
    model = Aroma
    success_url = reverse_lazy('productos')

class AromaDetailView(generic.DetailView):
    model = Aroma

class AromaListView(generic.ListView):
    model = Aroma
    template_name = 'templates/aromas/aroma_list.html'
    queryset = Aroma.objects.all()
    paginate_by = 5

def aroma_new(request):
    if request.method == "POST":
        form = AromaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('aroma_detail', pk=post.pk)
    else:
        form = AromaForm()
        return render(
        request,
        'Capilarte1/aroma_form.html', {'form': form})

def aroma_edit(request, pk):
    post = get_object_or_404(Aroma, pk=pk)
    if request.method == "POST":
        form = AromaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('aroma_detail', pk=post.pk)
    else:
        form = AromaForm(instance=post)
    return render(request, 'Capilarte1/aroma_form.html', {'form': form})

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('producto_detail', pk=post.pk)
    else:
        form = ProductoForm()
        return render(
        request,
        'Capilarte1/producto_form.html', {'form': form})

def producto_edit(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('producto_detail', pk=post.pk)
    else:
        form = ProductoForm(instance=post)
    return render(request, 'Capilarte1/producto_form.html', {'form': form})