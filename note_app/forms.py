from .models import User, Note
from django.forms import ModelForm


class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['username']

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note']