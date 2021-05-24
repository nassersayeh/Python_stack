from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(req):
    context = {
        "books" : Books.objects.all(),
        "authors" : Authours.objects.all()
    }
    return render(req,"index.html",context)
def addbook(req):
    title = req.POST['title']
    desc = req.POST['desc']
    Books.objects.create(title = title , desc = desc)
    return redirect("/")
def view(req,id):
    book_to_show = Books.objects.get(id=id)
    book_authours = book_to_show.authors.all()
    authours_show = Authours.objects.all()
    data = {
        'booktitle':book_to_show.title,
        'bookid' : book_to_show.id,
        'bookdesc':book_to_show.desc,
        'bookauthors':book_authours,
        'dropdwnauthors':authours_show
    }
    return render(req,"BooksView.html",data)
def addauthor(req,id):
    book= Books.objects.get(id=id)
    author = Authours.objects.get(id=req.POST['showauthor'])
    author.books.add(book)
    return  redirect("/")
def addauthors(req):
    context = {
        "authors" : Authours.objects.all(),
        
    }
    return render(req,"authors.html",context)
def addauthorsform(req):
    firstname = req.POST['firstname']
    lastname = req.POST['lastname']
    note = req.POST['note']
    Authours.objects.create(first_name = firstname,Last_name=lastname,note=note)
    return redirect("addauthors")
def show(req,id):
    author_to_show = Authours.objects.get(id=id)
    
    authours_show = Books.objects.all()
    data = {
        'firstname':author_to_show.first_name,
        'lastname' : author_to_show.Last_name,
        'authornote':author_to_show.note,
        'authorid':author_to_show.id,
        'dropdwnauthors':authours_show
    }
    return render(req,"AuthorView.html",data)
def addbooks(req,id):
    authoe= Authours.objects.get(id=id)
    book = Books.objects.get(id=req.POST['showbook'])
    book.authors.add(authoe)
    return  redirect("/")
