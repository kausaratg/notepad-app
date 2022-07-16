from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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
    starred = False
    context = {'user_note':user_note, 'user':user, 'starred':starred}
    return render(request, 'note_list.html', context)

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {'note':note}
    return render(request, 'note_detail.html', context)

def update_note(request, pk):
    note = Note.objects.get(id=pk)
    noteform = NoteForm(instance=note)
    context = {'noteform': noteform, 'note':note}
    if request.method == 'POST':
        update_post = NoteForm(request.POST, instance=note)
        if update_post.is_valid():
            update_post.save()
            return redirect(note_list)
    return render(request, 'update_note.html', context)

def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect(note_list)

def stared(request):
    is_starred = Note.objects.filter(status=1)
    context= {'user_note':is_starred}
    return render(request, 'stared_post.html', context)

def starred_notes(request, pk):
    note = get_object_or_404(Note, pk= request.POST.get('note_id'))
    starred = False
    if note.status == 0:
        note.status = 1
        note.save()
        starred = True
    else:
        note.status = 0
        note.save()
        starred = False
    return redirect('note_list')