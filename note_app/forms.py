from .models import User, Note
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

    def save(self, commit= True):
        user = super(Userform, self).save(commit=False)
        if commit :
            user.save()
        return user

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note']