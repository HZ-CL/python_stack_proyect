from show_app.models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


# Create your views here.
def new(request):
    return render(request, 'create.html')


def create(request):
    errors = Tv_show.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        Tv_show.objects.create(title = f'{title}', network=f'{network}', release_date=f'{release_date}', description=f'{description}')
        last_show = Tv_show.objects.last()
        id = last_show.id

        return redirect(f'/shows/{id}')


    #return HttpResponse('creacion en base de datos')

def show_id(request, id):
    context = {
        'show': Tv_show.objects.get(id=id)

    }
    return render(request, 'read_one.html', context)
    #return HttpResponse('muestra informacion del show')

def shows(request):
    context = {
        'data_shows': Tv_show.objects.all()
    }
    return render(request, 'read_all.html', context)
    #return HttpResponse('muestra todos los shows')

def show_id_edit(request, id):
    context = {
        'show': Tv_show.objects.get(id=id)
    }
    return render(request, 'update.html', context)
    #return HttpResponse('muestra la informacion para editar e id en link')

def show_id_update(request, id):
    errors = Tv_show.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        update = Tv_show.objects.get(id=id)
        update.title = request.POST['title']
        update.network = request.POST['network']
        update.release_date = request.POST['release_date']
        update.description = request.POST['description']
        update.save()

        return redirect(f'/shows/{id}')
    #return HttpResponse('para actualizar el registro en base de datos y redirige a /shows/id')

def show_id_destroy(request, id):
    show_destroy = Tv_show.objects.get(id=id)
    show_destroy.delete()

    return redirect('/shows')
    return HttpResponse('elimina el registro y redirije a /shows')

def raiz(request):
    return redirect('/shows')