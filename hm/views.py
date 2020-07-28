from django.shortcuts import render,redirect
from django.contrib import admin,messages
from django.contrib.auth.models import User,auth
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import Contact,Join

from django.http import HttpResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
import json
# Create your views here.

def home (request):
    return render(request,'hm/index.html')

def about (request):
    return render(request,'hm/index.html')

def business (request):
    return render(request,'hm/business.html')

def product(request):
    return render(request,'hm/product.html')

def rewards(request):
    return render(request,'hm/rewards.html')

def login(request):
    return render(request,'hm/login.html')

#def join (request):
#    thank = False
  #  if request.method == 'POST':
        #username = request.POST.get('email','')
        #fname = request.POST.get('fname', '')
        #lname = request.POST.get('lname', '')
        #mobn = request.POST.get('mobn', '')
        #spid = request.POST.get('spid', '')
        #gender = request.POST.get('gender', '')
        #state = request.POST.get('state', '')
       # password = request.POST.get('password', '')
       # email= request.POST.get('email', '')
        #print(fname, lname, spid, mobn, gender, state,email,password)
        #user = User.objects.create_user(username=email,email=email,password=password)
        #user.save()
        #join =Join( fname=fname, lname=lname, mobn=mobn, spid=spid,gender=gender, state=state, email=email, password=password)
        #join.save()
        #thank = True
    #return render(request,'hm/join.html')

def contact(request):
    thank = False
    if request.method=='POST':
        name = request.POST.get('name', '')
        whatsapp = request.POST.get('whatsapp', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        msg = request.POST.get('msg', '')
        print(fname, email, phone, msg,whatsapp,city)
        contact = Contact(name=name, email=email, phone=phone, msg=msg,whatsapp=whatsapp,city=city)
        contact.save()
        thank = True

    return render(request,'hm/contact.html',{'thank': thank})

def join(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user =User.objects.create_user(username=username,password=password,email=email)
        user.save();
        print('user created')
        return redirect("/")
    else :
        return render(request, 'hm/join.html')

