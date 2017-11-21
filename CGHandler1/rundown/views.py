# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os
import redis


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def loadMedias(request):
    path = "/home/tauwab/Desktop/CasparCG_Server/media"
    Files = os.listdir(path)
    if request.method == 'POST':
        '''
        filename = request.POST.get('name', None)
        namelist = []
        dict = {'name': filename,'image':filename +'.png'}
        namelist.append(dict)
        dict = {'name': 'abc', 'image': filename + '.png'}
        namelist.append(dict)
        dict = {'name': 'xyz', 'image': 'xyz.png'}
        namelist.append(dict)'''

        filename = request.POST.get('name', None)
        timestamp = '00:00:10:23'
        image = filename + '.png'
        '''
        redis_server = redis.Redis()
        entry = filename + " " + timestamp + " " + image
        entries = []
        entries.append(entry)
        redis_server.lpush('rundownlist', *entries)

        rundownlistSize = redis_server.llen('rundownlist')
        alldata = redis_server.lrange('rundownlist', 0, (rundownlistSize - 1))
        namelist = []
        for data in alldata:
            filename,timestamp,image = data.split()
            dict = {'name': filename, 'image': image, 'timestamp':timestamp}
            namelist.append(dict)
            '''
        namelist = []
        dict = {'name': filename, 'image': image, 'timestamp': timestamp}
        namelist.append(dict)
        return HttpResponse(json.dumps(namelist), content_type='application/json')
    return render(request,'rundown.html',{'Files':Files ,})


