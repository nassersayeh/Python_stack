from typing import Counter
from django.http import request
from django.shortcuts import redirect, render, HttpResponse, render_to_response
import random
rand = random.randint(1, 100)
def start(request):
    request.session['counter'] = 0
    request.session = rand
    return render(request,"index.html")



def index(request):
        context = []
        x = 0
        if request.method == 'POST' and request.POST.get('num'):
            x = int(request.POST.get('num'))
        print(rand)
        context = {
            'num': x,
            'rand':rand,
            'counter':request.session['counter']
        }
        if (x == rand):
            return render(request,"index.html",context = context)
        elif(x > rand):
            if 'counter' in request.session:
                request.session['counter'] +=1
            return render(request,"index.html",context= context)
        elif(x< rand):
            if 'counter' in request.session:
                request.session['counter'] +=1
            return render(request,"index.html",context = context)
            
        
        return render(request,"index.html", context = context)
    
def reset(resquest):
    resquest.session['counter'] = 0
    return redirect("/")

