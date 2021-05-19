from typing import Counter
from django.shortcuts import redirect, render, HttpResponse, render_to_response

def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
        return render(request,"index.html")    
    else:
        request.session['counter'] =0
        return render(request,"index.html")

def delete(request):
    del request.session['counter']
    return redirect("/")

def addtow(request):
    request.session['counter']+=1
    return redirect("/")

def userinput(request):
    request.session['counter']+= int(request.POST['num'])
    return redirect("/")