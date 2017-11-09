# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField("Name", max_length=250)
    password = models.CharField("password",max_length=250)
    email = models.EmailField()
    role = models.CharField(max_length=10,default='ROLE_USER')

    def __str__(self):
        return self.name #works as like toString(), return object string
