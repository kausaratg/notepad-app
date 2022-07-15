from django.db import models
from django.contrib.auth.models import User


user_name = User()
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title