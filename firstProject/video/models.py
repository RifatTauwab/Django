# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField("Title", max_length=250)
    embed_code = models.TextField("Embed code")

    def __str__(self):
        return self.title #works as like toString(), return object string