# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .commands.manageserver import play
from .commands.redispub import pub_play
import redis
# Create your views here.



def displayMedias(request):
    path = "/home/tauwab/Desktop/CasparCG_Server/media"
    Files = os.listdir(path)
    return render(request,'displaymedias.html',{'Files':Files ,})

def runMedia(request,fileName):
    path = "/home/tauwab/Desktop/CasparCG_Server/media"
    Files = os.listdir(path)
    return render(request,'displaymedias.html',{'Files':Files , 'name':fileName,})

def serverHandler(request,fileName):
    cmd = "play 1-10 %s"%(fileName)
    pub_play(cmd)
    return HttpResponseRedirect(reverse('displayMedias'))
