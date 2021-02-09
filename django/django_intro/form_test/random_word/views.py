from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

def pag(request):
    request.session['counter']=0
    return render(request, 'random_w.html')


def random_pag(request):
    request.session['counter'] += 1
    context={
        "generated" : get_random_string(length=14)
    }
    return render(request, 'random_w.html', context)

def reset(request):
    return redirect('/random_word')

# Create your views here.
