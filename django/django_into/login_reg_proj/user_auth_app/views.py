from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from user_auth_app.models import User

def index (req):
    if 'user' in req.session:
        return redirect('/welcome')
    return render(req,"index.html")
def login(req):
    email = req.POST['email']
    passwd = req.POST['passwd']
    
    users = User.objects.filter(email=email)
    
    if len(users) == 0:
        return redirect("/")
    user = users.first()
    if user.password != passwd:
        return redirect("/")
    data ={
        'username' : user.username,
        'password':user.password,
        'email' : user.email,
        'adress' : user.adress
    }
    req.session['user']= data
    return redirect("/welcome")

def reg(req):
    email = req.POST['email2']
    passwd = req.POST['passwd2']
    username = req.POST['username']
    address = req.POST['adress']
    data ={
        'username' : username,
        'password':passwd,
        'email' : email,
        'adress' : address
    }
    User.objects.create(username = username , password = passwd , email = email , adress = address)
    data ={
        'username' : username,
        'password':passwd,
        'email' : email,
        'adress' : address
    }
    req.session['user']= data
    return redirect('/welcome')
def welc (req):
    if req.session['user']:
        user = req.session['user']
        return render(req,"welcome.html",user)
    return redirect('/')
def logout(req):
    if req.session['user']:
        req.session.clear()
    return redirect('/')