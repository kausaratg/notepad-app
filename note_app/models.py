from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User


user_name = User()
# Create your models here.
class Note(models.Model):
    STATUS = (
        (0, 'not_starred'),
        (1, 'is_starred'),
    )
    username = models.ForeignKey(user_name, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    note = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title