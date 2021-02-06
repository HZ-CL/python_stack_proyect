from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect('blogs/')

def index(request):
    return HttpResponse("(def index)placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("(def new)placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def creation(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request, number):
    return redirect('/blogs')