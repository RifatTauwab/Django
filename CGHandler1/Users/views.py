# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Users
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

def createuser(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)

        # users  = Users(name=username,password=password,email=email)
        # users.save()

        #if we want to create django user
        # store user into auth_user table
        #user = User()
        user = User.objects.create_user(username=username,password=password,email=email) #this line already create an user
        user.last_name = 'last' #to modify user
        user.save()

    return render(request, 'createuser.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                return redirect("/")
            else:
                return HttpResponse("login failed")
        else:
            return HttpResponse("Username or Password can not be empty")
    return render(request,'login.html')

def displayUsers(request):
        allUsers = Users.objects.all()
        #specific column Users.objects.values_list('id', 'name')
        #specific column Users.objects.values('name')
        #condition LIKE %ar% Users.objects.get(name__contains='ar')
        #condition name = 'abc' Users.objects.get(name__exact="abc")
        #condition where id <= 5 Users.objects.filter(id__lte=5)
        #condition LIMIT 5 Users.objects.all()[:5]
        # ORDER BY Users.objects.order_by('id')[0]
        return render(request, 'displayusers.html', {'users': allUsers})

class MyView(View):
    def get(self, request):
        return HttpResponse('result')