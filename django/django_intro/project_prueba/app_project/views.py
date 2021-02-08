from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Hello Word!")

# Create your views here.
