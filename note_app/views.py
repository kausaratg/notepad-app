from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Note, User
from .forms import Userform, NoteForm
from django.shortcuts import redirect
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect(note)
        messages.info(request, 'unsuccessful registration: invalid information')
    context = {'form':form}
    return render(request, 'index.html', context )

def signin(request):
    form = AuthenticationForm()
    context = {'form':form}
    if request.method == 'POST':
        form_user = AuthenticationForm(request, data=request.POST)
        if form_user.is_valid():
            username = form_user.cleaned_data.get('username')
            password = form_user.cleaned_data.get('password')
            form_name =authenticate(username=username, password = password)
            if form_name is not None:
                login(request, form_name)
                return redirect('note_list')
        else:
            messages.info(request, 'invalid information')
            return redirect('signin')
    return render(request, 'signin.html', context)

@login_required
def note(request):   
    noteform = NoteForm()
    if request.method == "POST":
        note = NoteForm(request.POST)
        if note.is_valid():
          note_check = note.save( commit=False)
          note_check.username = request.user
          note_check.save()
        return redirect(note_list)
    context = {'noteform':noteform}
    return render(request, 'notes.html', context)

@login_required(login_url='signin')
def note_list(request):
    user_note = Note.objects.filter(username= request.user)
    user = request.user
    starred = False
    context = {'user_note':user_note, 'user':user, 'starred':starred}
    return render(request, 'note_list.html', context)

@login_required(login_url='signin')
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {'note':note}
    return render(request, 'note_detail.html', context)

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect(note_list)

@login_required(login_url='signin')
def stared(request):
    # login_user = Note.objects.filter(request.user)
    is_starred = Note.objects.filter(username = request.user, status=1)
    context= {'user_note':is_starred}
    return render(request, 'stared_post.html', context)

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def log_me_out(request):
    logout(request)
    return redirect('/')
