# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from Media.models import Media, Media_Statistics
from Media.serializer import MediaSerializer, Media_StatisticsSerializers
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

@csrf_exempt
def MediaListApi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def MediaApi(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        media = Media.objects.get(id=id)
    except Media.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MediaSerializer(media, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        media.delete()
        return HttpResponse(status=204)


class MediaStatisticsViewSet(ModelViewSet):
    queryset = Media_Statistics.objects.all()
    serializer_class = Media_StatisticsSerializers

router = DefaultRouter()
router.register('mediastat',MediaStatisticsViewSet)