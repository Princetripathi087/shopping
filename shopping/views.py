from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Mobilep,Elec,Home,Homedeal,Mobilesp,Elecs,Product
# Create your views here.
def index(request):
    hom=Home.objects.all()
    homd=Homedeal.objects.all()
    return render(request,'index.html',{'hom':hom,'homd':homd})

def signin(request):
    return render(request,'signin.html')

def register(request):
    return render(request,'register.html')

def Products(request):
    p=Product.objects.get()
    return render(request,'Products.html',{'p':p})

def cart(request):
    return render(request,'cart.html')

def account(request):
    return render(request,'account.html')

def electronics(request):
    ele=Elec.objects.all()
    es=Elec.objects.all()
    return render(request,'electronics.html',{'ele':ele,'es':es})

def mobile(request):
    
    mobp=Mobilep.objects.all()
    mf=Mobilesp.objects.all()
    #dish = Mobilep.objects.filter(id = Mobilesp.Mimg).first()

    return render(request,'mobile.html',{'mobp':mobp,'mf':mf})

def oneplus(request,mid):
    mf=Mobilesp.objects.get(id=mid)
    return render(request,'oneplus.html',{'mf':mf})

def product(request):
    return render(request,'product-details.html')

def redmi(request):
    return render(request,'redmi.html')

def samsung(request):
    return render(request,'samsung.html')

def elecspc(request,i):
    es=Elecs.objects.get(id=i)
    return render(request,'elecspc.html',{'es':es})