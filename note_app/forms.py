from .models import User
from django.forms import ModelForm


class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['username']