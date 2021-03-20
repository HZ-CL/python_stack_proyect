from django.db import models
from django.db.models.manager import Manager
from datetime import datetime, date
import re
import bcrypt
# Create your models here.

class UsuarioManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        #validar First name
        fname = re.compile(r'^[a-zA-Z]+$')
        if not fname.match(postData["fname"]):
            errors["fname"] = "solo puede introducir letras en el nombre"
        if len(postData['fname'])<2:
            errors["fname_2"] = "El nombre tiene que tener almenos 2 caracteres"
        #validar apellido
        if not fname.match(postData["lname"]):
            errors["lname"] = "solo puede introducir letras en el apellido"
        if len(postData["lname"])<2:
            errors["lname_2"] = "El apellido tiene que tener almenos 2 caracteres"
        #validar email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['regis_email']):
            errors["regis_email"] = "Email invalido."
        email_is = Usuarios.objects.filter(cuenta__email__icontains=postData['regis_email'])
        if len(email_is)>0:
            errors["regis_email_2"] = "Email ya esta registrado"

        #validar contraseña
        if len(postData["psw"])<8:
            errors["psw"] = "Contarseña debe tener al menos 8 caracteres"
        elif postData["psw"] != postData["re_psw"]:
            errors["re_psw"] = "Contraseñas no coinciden"
        #validar cumpleaños
        if len(postData['brithday'])>0:
            hoy=datetime.today()
            cumple = date.fromisoformat(postData['brithday'])
            años = hoy.year - cumple.year
            if años<=13:
                errors['brithday'] = 'Debe ser mayor a 13 años'
        else:
            errors['britday'] = 'debe ingresar una fecha de cumpleaños'

        return errors

    def password_hash(self, postData):
        hash1 = bcrypt.hashpw(postData['psw'].encode(), bcrypt.gensalt()).decode()
        return hash1



class Cuentas(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Usuarios(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cumpleaño = models.DateField(max_length=25)
    cuenta = models.ForeignKey(Cuentas, related_name= 'usuario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsuarioManager()