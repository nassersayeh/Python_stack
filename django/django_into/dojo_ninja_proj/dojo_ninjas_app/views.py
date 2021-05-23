from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(req):
    context = {
        "dojonames":Dojo.objects.all(),
        "dojos" : Dojo.objects.all(),
        "ninjas":Ninjas.objects.all()
    }
    return render(req,"index.html",context)
def AddDojo(req):
    Dojo.objects.create(name = req.POST['name'], city = req.POST['city'],state = req.POST['state'])
    return redirect('/')
def AddNinja(req):
    Ninjas.objects.create(first_name= req.POST['firstname'],last_name = req.POST['lastname'], dojo = Dojo.objects.get(name=req.POST['dojo']))
    return redirect('/')
def delete(req):
    Dojo.objects.filter(name=req.POST['dojo']).delete()
    return redirect('/')
