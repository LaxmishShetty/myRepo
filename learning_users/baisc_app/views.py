# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from baisc_app.forms import UserProfielInfoForm,UserForm
from django.shortcuts import render
from baisc_app.forms import UserForm,UserProfielInfoForm
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'baisc_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Its a special page ")


def register(request):

    registered=False

    if request.method=="POST":
         user_info=UserForm(data=request.POST)
         profile_info=UserProfielInfoForm(request.POST)

         if user_info.is_valid() and profile_info.is_valid():

             user=user_info.save()
             user.set_password(user.password)
             user.save()

             profile=profile_info.save(commit=False)
             profile.user=user

             if 'profile_pic' in request.FILES:

                 profile.profile_pic=request.FILES['profile_pic']

                 profile.save()

             registered=True

         else:
            print user_info.errors,profile_info.errors

    else:
        user_info=UserForm()
        profile_info=UserProfielInfoForm

    return render(request,'baisc_app/registration.html',{"user_info":user_info,"profile_info":profile_info,"registered":registered})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))

            return HttpResponse("User not active")
        else:
            print "Not authenticated"
            print "Username:{} and password:{}".format(username,password)

    return render(request,'baisc_app/login.html',{})



