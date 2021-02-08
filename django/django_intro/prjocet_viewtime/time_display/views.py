from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def root(request):
    return redirect('/time_display')
    #return HttpResponse("punto de que entre")

def reloj(request):
    context = {
        "time" : strftime("%b %d, %Y", gmtime()),
        "watch" : strftime("%H:%M %p", gmtime())

    }
    return render(request, "index.html", context)
    #return HttpResponse("def reloj")

# Create your views here.
