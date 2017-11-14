# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Media.models import Media, Media_Statistics

admin.site.register(Media)
admin.site.register(Media_Statistics)
