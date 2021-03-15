from django.db import models

# Create your models here.
class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=8)
    description = models.TextField(default=000-00-00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
