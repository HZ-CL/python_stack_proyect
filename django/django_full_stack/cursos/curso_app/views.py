from django.shortcuts import render, redirect
from curso_app.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    context = {
        'curso': cursos,
    }

    return render(request, 'home.html', context)

def destroy(request, id):
    destroy_curso = Curso.objects.get(id=id)
    context = {
        'curso': destroy_curso
    }

    return render(request, 'destroy.html', context)

def delete(request):
    curso_id = request.POST['id']
    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect('/')

def create(request):
    errors = Curso.objects.validar(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        name = request.POST['name']
        description = request.POST['description']
        Curso.objects.create(name=f'{name}', description=f'{description}')

        return redirect('/')
