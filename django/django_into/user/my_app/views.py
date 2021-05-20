from django.shortcuts import redirect, render
# other imports
from .models import user
# show all of the data from a tablecopy
def index(request):
    context = {
        "all_the_user": user.objects.all()
    }
    return render(request, "index.html", context)

def adduser(request):
    user.objects.create(firstname = request.POST['firstname'] , lastname = request.POST['lastname'] , email = request.POST['email'], age = request.POST['age'])
    return redirect('/')