from django.shortcuts import redirect, render
from .models import*
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.utils import timezone
def home(req):
    req.session['user'] = ""
    return render(req,"home.html")
def create(req):
    errors = User.objects.basic_validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        email = req.POST['email']
        passwd = req.POST['passwd']
        confpw = req.POST['confirmpw']
        birthDate = req.POST['birth_date']
        try:
            if User.objects.get(email=email):
                errors["retitle"] = "this email is already exist"
        except:
            pass
        
        
        if passwd == confpw :
            User.objects.create(first_name=firstname,last_name=lastname,email=email,passwod=passwd)
            data ={
                "fname":firstname,
                "lastname":lastname,
                "email": email,
                "pass":passwd,
                "birth_date": birthDate
            }
            req.session['user'] = data
            return redirect('/welcome')
        return redirect("/")
def login(req):
    email = req.POST['loginemail']
    passwd = req.POST['loginpass']
    users = User.objects.filter(email=email)
    if len(users) == 0:
        return redirect("/")
    user = users.first()
    if user.passwod != passwd:
        return redirect("/")
    data ={
        'fname' : user.first_name,
        'password':user.passwod,
        'email' : user.email,
        'lastname' : user.last_name
    }
    req.session['user']= data
    return redirect("/welcome")

def welc(req):
    if req.session['user']:
        user = req.session['user']
        return render(req,"welcome.html",user)
    return redirect('/')
def logout(req):
    if req.session['user']:
        req.session.clear()
        return redirect('/')
