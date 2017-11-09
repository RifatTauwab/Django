# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from .serializers import VideoSerializers

from .models import Video

# Create your views here.

def home(request):
    #return HttpResponse("Hello World")
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request,'home.html',{'last_video':last_video})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                return redirect("/")
            else:
                return HttpResponse("login faild")
        else:
            return HttpResponse("Username or Password can not be empty")
    return render(request,'login.html')

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

router = DefaultRouter()
router.register('video',VideoViewSet) #/api/video/1 /api/video/2
