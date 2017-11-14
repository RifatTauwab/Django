# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()

# python manage.py makemigrations
# python manage.py migrate

class Media(models.Model):
    name = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=8,default='ACTIVE')

    def __str__(self):
        return self.name+" "+self.status #works as like toString(), return object string

class Media_Statistics(models.Model):
    name = models.CharField(max_length=250)
    played = models.IntegerField()

    def __str__(self):
        return self.name+" "+str(self.played) #works as like toString(), return object string
