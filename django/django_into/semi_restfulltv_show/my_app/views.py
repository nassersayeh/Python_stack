from django.shortcuts import redirect, render
from django.contrib import messages
from .models import*

def index(req):
    context={
        "Shows": Show.objects.all()
    }
    return render(req,"main.html",context)
def show(req):
    return render(req,"addshow.html")
def addshow(req):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/show')
    else:
        title = req.POST['showtitle']
        network = req.POST['network']
        releasedate = req.POST['releasedate']
        desc = req.POST['desc']
        Show.objects.create(title=title,network=network,releasedate=releasedate,desc=desc)
        last = Show.objects.last()
        id = last.id
        messages.success(req, "Show successfully updated")
        return redirect('showtv/'+str(id))
def showtv(req,id):
    showid = Show.objects.get(id=id)
    
    context={
        'showid':showid.id,
        'showtitle':showid.title,
        'showdesc':showid.desc,
        'showreles':showid.releasedate
    }
    return render(req,"showtv.html",context)
def showedit(req,id):
    showid = Show.objects.get(id=id)
    context ={
        'showid':showid.id,
        'showtitle':showid.title,
        'showdesc':showid.desc,
        'showreles':showid.releasedate
    } 
    return render(req,"editshow.html",context)
def edit(req,id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(req.POST)
    last = Show.objects.get(id=id)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/showtv/'+str(last.id)+'/edit')
    title = req.POST['showtitle']
    network = req.POST['network']
    releasedate = req.POST['releasedate']
    desc = req.POST['desc']
    
    Show.objects.filter(id=last.id).update(title=title,network=network,releasedate=releasedate,desc=desc)
    last2 = Show.objects.get(id=id)
    context ={
        'showid':last2.id,
        'showtitle':last2.title,
        'showdesc':last2.desc,
        'showreles':last2.releasedate,
        
    }
    messages.success(req, "Show successfully updated")
    return render(req,"showtv.html",context)
def destroy(req,id):
    Show.objects.filter(id=id).delete()
    return redirect('/shows')

def update(request, id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        show = Show.objects.get(id = id)
        show.title = request.POST['showtitle']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
        # redirect to a success route
        return redirect('/showtv/'+str(show.id))
