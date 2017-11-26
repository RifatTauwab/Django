# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Websites(models.Model):
    link = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
    keywords = models.CharField(max_length=250)

    def __str__(self):
        return self.title #works as like toString(), return object string

