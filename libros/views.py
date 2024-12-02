from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Vista para agregar un nuevo libro
@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')  # Redirige a la lista de libros
    else:
        form = BookForm()
    
    return render(request, 'libros/agregar_libro.html', {'form': form})

# Vista para ver todos los libros
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})
