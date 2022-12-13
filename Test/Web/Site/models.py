from django.db import models


# Create your models here.


class football(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos')
    image_top = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()

    def __str__(self):
        return self.name
