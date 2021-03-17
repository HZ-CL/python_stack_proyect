from django.db import models
from datetime import datetime
print(datetime.today())

# Create your models here.
class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = 'title should be at least 2 characters!'

        if len(postData['network'])<3:
            errors['networ'] = 'networks should be at least 3 characters!'

        if len(postData['release_date'])<8:
            errors['release_date'] = 'enter a release date.'

        if len(postData['description']) == 0:
            errors['description'] = 'you have to write a description!'

        if len(postData['description'])<10:
            errors['description_10'] = 'description should be at least 10 characters!'


        return errors





class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=8)
    description = models.TextField(default=000-00-00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvManager()
