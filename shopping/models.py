from typing import KeysView
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Mobilep(models.Model):
    Mimg = models.ImageField(upload_to='pics')
    Mname = models.TextField()
    Mprice = models.IntegerField()

class Elec(models.Model):
    
    Eimg = models.ImageField(upload_to='pics')
    Ename = models.TextField()
    Eprice = models.IntegerField()

class Home(models.Model):
    
    Himg = models.ImageField(upload_to='pics')
    Hname = models.TextField()
    Hprice = models.IntegerField()

class Homedeal(models.Model):
    
    Hdimg = models.ImageField(upload_to='pics')
    Hdname = models.TextField()
    Hdprice = models.IntegerField()

class Mobilesp(models.Model):
    Mimg = models.ImageField(upload_to='pics')
    Mname = models.TextField()
    Mprice = models.IntegerField()
    Mstyle=models.TextField()
    Mcolor=models.TextField()
    Mcamera=models.TextField()
    Msize=models.TextField()
    Mmemory=models.TextField()
    Mbattry=models.TextField()
    Mwarranty=models.TextField()
    Mother=models.TextField()
    
class Indexs(models.Model):
    Isimg = models.ImageField(upload_to='pics')
    Isname = models.TextField(max_length=50, default="", editable=False)
    Isprice = models.IntegerField()
    Issize = models.IntegerField()
    Iscolor = models.TextField()

class Elecs(models.Model):
    Esimg = models.ImageField(upload_to='pics')
    Esname = models.TextField()
    Esprice = models.IntegerField()
    Essize = models.TextField()
    Esother = models.TextField()

class Featspc(models.Model):
    Fsimg = models.ImageField(upload_to='pics')
    Fsname = models.TextField()
    Fsprice = models.IntegerField()
    Fssize = models.TextField()
    Fsother = models.TextField()

class Product(models.Model):
    Pimg = models.ImageField(upload_to='pics')
    Pname = models.TextField()
    Pprice = models.IntegerField()