from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from books_authors_app.models import *


# Create your views here.
def view_books(request):
    libreria = Libro.objects.all() #descargo la lista de libros en base de datos
    context = {
        'lista' : libreria # envio todos los libros
    }

    return render(request, 'add_book.html', context)

def add_book(request):
    dato_titulo_form = request.POST['titulo_libro']             #extraigo el dato del titulo
    dato_descripcion_form = request.POST['descripcion_libro']   #extraigo el dato de la discripcion
    Libro.objects.create(title = f'{dato_titulo_form}', desc = f'{dato_descripcion_form}') #creo el libro en la base de datos

    return redirect('/')

def book_info(request, id_book):

    abrir_libro = Libro.objects.get(id=id_book) #obtengo la informacion del libro
    autor_libro = abrir_libro.libros_autores.all() #obtengo los autores asociados al libro
    lista_autores = Autor.objects.all().exclude(libros=id_book)#recupero los autores y excluyo a los autores que ya estan asociados
    context = {
        'info_libro' : abrir_libro,             #envio info del libro
        'autor' : autor_libro,                  #envio info de los autores del libro
        'autores_despliege' : lista_autores     #envio los autores restantes
    }
    return render(request, 'view_book.html', context)

def asignando_autor(request, id_book):
    id_autor = request.POST['id_autor'] #obtengo el id del autor para asignar al libro
    autor_asig = Autor.objects.get(id=id_autor)
    id_libro = Libro.objects.get(id=id_book)    #obtengo id del libro
    autor_asig.libros.add(id_libro) # ORM para asiganar autor-libro

    return redirect(f'/view_book/{id_book}')