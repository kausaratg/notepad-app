from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note', views.note, name='note'),
]
