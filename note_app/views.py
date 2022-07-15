from django.shortcuts import render
from .models import Note, User
from .forms import Userform, NoteForm
from django.shortcuts import redirect
from  django.contrib.auth.models import auth

# Create your views here.
def index(request):
    userform = Userform()
    if request.method =='POST':
        user = ""
        user_check = Userform(request.POST or None)
        if user_check.is_valid():
            name = user_check.save()
            user = name
        user_note = Note.objects.all()
        context = {'user':user, 'user_note':user_note}
        return render(request, 'note_list.html', context)
    context = {'userform':userform}
    return render(request, 'index.html', context)

def note(request):   
    noteform = NoteForm()

    if request.method == "POST":
        note = NoteForm(request.POST)
        if note.is_valid():
            note.save()
        return redirect(note_list)
    context = {'noteform':noteform}
    return render(request, 'notes.html', context)


def note_list(request):
    user_note = Note.objects.all()
    user = request.user
    context = {'user_note':user_note, 'user':user}
    return render(request, 'note_list.html', context)

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {'note':note}
    return render(request, 'note_detail.html', context)
