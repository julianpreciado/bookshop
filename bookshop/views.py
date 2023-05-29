from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import libro
from .forms import libroform
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros = libro.objects.all()
    return render(request,'libros/index.html', {'libros': libros})

def crear(request):
    formulario = libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    Libro=libro.objects.get(id=id)
    formulario = libroform(request.POST or None, request.FILES or None, instance=Libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario': formulario})

def eliminar(request, id):
    Libro = libro.objects.get(id=id)
    Libro.delete()
    return redirect('libros')