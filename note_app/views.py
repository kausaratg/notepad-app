from django.shortcuts import render
from .models import Note, User
from .forms import Userform

# Create your views here.
def index(request):
    userform = Userform()
    if request.method =='POST':
        user_check = Userform(request.POST)
        if user_check.is_valid():
            user_check.save()
            user = User()
            context = {'user':user}
            return render(request, 'notes.html', context)
    context = {'userform':userform}
    return render(request, 'index.html', context)

def note(request):   
    return render(request, 'notes.html')
