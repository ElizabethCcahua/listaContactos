from django.shortcuts import render, redirect
from .forms import ReviewForm
from .forms import BookForm
from .models import Book
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


# Vista para agregar una reseña a un libro
@login_required
def agregar_review(request, libro_id):
    libro = Book.objects.get(id=libro_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Asocia la reseña con el usuario logueado
            review.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = ReviewForm()

    return render(request, 'libros/agregar_review.html', {'form': form, 'libro': libro})
