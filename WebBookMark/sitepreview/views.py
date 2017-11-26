# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from bs4 import BeautifulSoup
import urllib
import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from sitepreview.models import Websites
from sitepreview.serializer import WebsitesSerializer


@csrf_exempt
def home(request):
    if request.method == 'POST':
        url = request.POST.get('url', None)
        #page = urllib.urlopen(url).read()
        agent = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=agent).text
        soup = BeautifulSoup(page,'html.parser')

        try:
            title = soup.find("title").text
        except:
            title = "no title found"
        try:
            try:
                desc = soup.find("meta", property="og:description")['content'].encode('utf-8')
            except:
                try:
                    desc = soup.find(attrs={'name': 'Description'})['content'].encode('utf-8')
                except:
                    desc = soup.find(attrs={'name': 'description'})['content'].encode('utf-8')
        except:
            desc = "no description  found"
        try:
            image = soup.find("meta", property="og:image")['content'].encode('utf-8')
        except:
            image = "http://www.bsmc.net.au/wp-content/uploads/No-image-available.jpg"

        try:
            try:
                keywords = soup.find(attrs={'name': 'Keywords'})['content'].encode('utf-8')
            except:
                keywords = soup.find(attrs={'name': 'keywords'})['content'].encode('utf-8')
            if keywords == '':
                keywords = 'NA'
        except:
            keywords = "NA"

        namelist = []
        dict = {'title': title, 'desc': desc, 'image': image, 'keywords':keywords, 'url':url,}
        namelist.append(dict)
        return HttpResponse(json.dumps(namelist), content_type='application/json')
    # try:
    #     websites = Websites.objects.all()
    # except Websites.DoesNotExist:
    #     return HttpResponse(status=404)
    #
    # if request.method == 'GET':
    #     serializer = WebsitesSerializer(websites)

    return render(request,'home.html',)

class WebsitesViewSet(ModelViewSet):
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer

router = DefaultRouter()
router.register('websites',WebsitesViewSet)