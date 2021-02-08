from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    #return HttpResponse("Esta es la equivalente de APP directorio / raiz")
    return redirect("home/")

def home(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)