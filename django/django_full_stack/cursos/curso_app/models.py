from django.db import models



class CursoManager(models.Manager):
    def validar(self, postData):
        errors = {}
        if len(postData['name'])<5:
            errors['name'] = 'el nombre ingresado debe tener más de 5 caracteres'
        if len(postData['description'])<15:
            errors['description'] = 'descripción debe tener más de 15 caracteres'

        return errors

# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CursoManager()