from django.shortcuts import redirect, render
from django.contrib import messages
from login_app.models import *
import bcrypt

# Create your views here.

def logregistro(request):
    return render(request, 'login_registro.html')

def validar(request):
    errors = Usuarios.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password_hash = Usuarios.objects.password_hash(request.POST)
        cuenta_user = Cuentas.objects.create(email = request.POST['regis_email'], password = password_hash)
        Usuarios.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], cumpleaño = request.POST['brithday'], cuenta = cuenta_user)


        #el log despues de registrar
        users = Usuarios.objects.get(cuenta__email__icontains=request.POST['regis_email'])
        request.session['loginuser'] = request.POST['regis_email']
        request.session['usermail'] = request.POST['regis_email']
        request.session['username'] = f"{users.first_name} {users.last_name}"
        request.session['userid'] = f"{users.cuenta.id}"

    return redirect('/successlink')

def login(request):
    if request.method == "POST":
        user = Usuarios.objects.filter(cuenta__email__icontains=request.POST['log_email'])
        if len(user)>0:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['log_psw'].encode(), logged_user.cuenta.password.encode()):
                request.session['loginuser'] = request.POST['log_email']
                request.session['username'] = f"{logged_user.first_name} {logged_user.last_name}"
                request.session['useremail'] = f"{logged_user.cuenta.email}"
                request.session['userid'] = f"{logged_user.cuenta.id}"
                return redirect('/successlink')
            else:
                errors_c = {
                    'contraseña':'contraseña incorrecta'
                }
                for key, value in errors_c.items():
                    messages.error(request, value)
                return redirect('/')
        errors_e = {
            'contraseña':'Cuenta no registrada'
            }
        for key, value in errors_e.items():
            messages.error(request, value)
        return redirect('/')

        #error_log = Usuarios.objects.login(request.POST)
        #if len(error_log) > 0:
        #    for key, value in error_log.items():
        #        messages.error(request, value)
        #    return redirect('/')
        #else:
        #    request.session['loginuser'] = request.POST['log_email']
        #    users = Usuarios.objects.get(cuenta__email__icontains=request.POST['log_email'])
        #    request.session['username'] = f"{users.first_name} {users.last_name}"
        #    request.session['useremail'] = f"{users.cuenta.email}"
        #    request.session['userid'] = f"{users.cuenta.id}"

        #return redirect('/successlink')
    #return redirect('/')


def success(request):
    if len(request.session['loginuser'])>0:
        return render(request, 'success.html')
    messages.error (request,'Debe iniciar sesión o registrarse para ingresar')
    return redirect('/')

def logout(request):
    request.session['loginuser'] = ''
    request.session['username'] = ''
    request.session['useremail'] = ''
    request.session['userid'] = 0
    messages.error (request,'Se ha cerrado sesión')
    return redirect('/')
