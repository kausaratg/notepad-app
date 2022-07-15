from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note', views.note, name='note'),
    path('note_list', views.note_list, name='note_list'),
]
