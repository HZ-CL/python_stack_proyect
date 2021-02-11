from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    #return HttpResponse("entramos a index")
    #request.session['name'] = request.POST['name']
    #request.session['counter'] = 100
    request.session['counter']=0
    print(request.session["counter"])
    request.session['actividad']= []

    return render(request, "index.html")

def process_money(request, link):


    if link == "farm":
        gold=random.randint(10, 20)
        request.session['counter'] +=gold
        time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
        linea_ms = {
            "clase":"gano", "ms": f"Earned ${gold} golds from the {link}! {time}"
        }
        request.session['actividad'].append(linea_ms)
        return render(request, "index.html")


    if link == "cave":
        gold=random.randint(5, 10)
        request.session['counter'] +=gold
        time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
        linea_ms = {
            "clase":"gano", "ms": f"Earned ${gold} golds from the {link}! {time}"
        }
        request.session['actividad'].append(linea_ms)
        return render(request, "index.html")


    if link == "house":
        gold=random.randint(2, 5)
        request.session['counter'] +=gold

        time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
        linea_ms = {
            "clase":"gano", "ms": f"Earned ${gold} golds from the {link}! {time}"
        }
        request.session['actividad'].append(linea_ms)


        return render(request, "index.html")

    if link == "casino":
        gold=random.randint(-50, 50)
        request.session['counter'] +=gold


        if gold > 0:
            time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
            linea_ms = {
                "clase":"gano", "ms": f"you have won ${gold} golds from the {link}! {time}"
            }
            request.session['actividad'].append(linea_ms)


        elif gold < 0:
            time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
            linea_ms = {
                "clase":"perdio", "ms": f"Entered a {link} an lost ${gold} golds... Ouch! {time} "
            }
            request.session['actividad'].append(linea_ms)


        else:
            time = strftime("(%Y/%m/%d %I:%M:%S %p)", gmtime())
            linea_ms = f"Entered a {link} no profit! {time} "
            linea_ms = {
                "clase":"nada", "ms": f"Entered a {link} no profit! ${gold} :( {time} "
            }
            request.session['actividad'].append(linea_ms)


        return render(request, "index.html")


